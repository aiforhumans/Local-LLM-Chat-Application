import gradio as gr
from openai import OpenAI
import tiktoken

def create_client(base_url="http://localhost:1234/v1", api_key="dummy_key"):
    return OpenAI(
        base_url=base_url,
        api_key=api_key  # Allows flexibility for API key and base URL
    )

def prepare_chat_params(model_name, messages, temperature=0.7, max_tokens=1000, top_p=1, frequency_penalty=0, presence_penalty=0, stream=True):
    return {
        "model": model_name,
        "messages": messages,
        "temperature": temperature,
        "max_tokens": max_tokens,
        "top_p": top_p,
        "frequency_penalty": frequency_penalty,
        "presence_penalty": presence_penalty,
        "stream": stream
    }

def count_tokens(messages, model="gpt-3.5-turbo-0301"):
    encoding = tiktoken.encoding_for_model(model)
    num_tokens = 2  # starting with primed reply tokens

    for message in messages:
        num_tokens += 4  # <im_start>{role/name}\n{content}<im_end>\n
        for key, value in message.items():
            token_count = len(encoding.encode(value))
            num_tokens += token_count if key != "name" else (token_count - 1)

    return num_tokens

def chatbot(message, history):
    client = create_client()
    model_name = "llama3-8B-DarkIdol-2.1-Uncensored-32K-GGUF"

    # Construct the message history
    messages = [{"role": "system", "content": "Summarize the question and provide a response."}]
    messages += [{"role": role, "content": content} for h in history for role, content in [("user", h[0]), ("assistant", h[1])]]
    messages.append({"role": "user", "content": message})

    # Token counting
    if count_tokens(messages) > 4000:  # Model token limit check
        yield "I apologize, but the conversation has become too long. Please start a new conversation."
        return

    # Prepare chat parameters
    chat_params = prepare_chat_params(model_name, messages)
    
    try:
        # Stream responses using synchronous iteration
        completion = client.chat.completions.create(**chat_params)
        full_response = ""
        for chunk in completion:
            content = chunk.choices[0].delta.content
            if content:
                full_response += content
                yield full_response.strip()
    except Exception as e:
        yield f"An error occurred: {str(e)}"

# Create and launch the Gradio interface
iface = gr.ChatInterface(
    fn=chatbot,
    title="OpenAI Chatbot (Streaming)",
    description="Chat with an AI assistant using your local OpenAI setup. Responses are streamed in real-time.",
    examples=["Can you explain the basics of Gradio?", "How can I create a simple Gradio app?"],
    retry_btn=None,
    undo_btn="Delete Previous",
    clear_btn="Clear",
)

if __name__ == "__main__":
    iface.launch(share=True)
