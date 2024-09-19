from openai import OpenAI
import os


def create_client():
    base_url = "http://localhost:1234/v1"
    return OpenAI(
        base_url=base_url,
        api_key="dummy_key"  # The API key can be any non-empty string for the local LLM
    )


def prepare_chat_params(model_name, messages):
    return {
        "model": model_name,
        "messages": messages,
        "temperature": 0.7,
        "max_tokens": 1000,
        "top_p": 1,
        "frequency_penalty": 0,
        "presence_penalty": 0,
        "stream": True,
    }


def process_streamed_response(completion):
    full_response = ""
    for chunk in completion:
        if chunk.choices[0].delta.content is not None:
            content = chunk.choices[0].delta.content
            full_response += content
            print(content, end="", flush=True)
    return full_response


def main():
    try:
        client = create_client()
        model_name = "gpt-3.5-turbo"  # Replace with your local model name if different
        messages = [
            {"role": "system", "content": "You are a Gradio developer expert"},
            {"role": "user", "content": "Can you explain the basics of Gradio?"},
            {"role": "assistant", "content": "Sure, for what are you using Gradio?"},
            {"role": "user", "content": "I want to chat with OpenAI?"}
        ]

        chat_params = prepare_chat_params(model_name, messages)
        completion = client.chat.completions.create(**chat_params)

        full_response = process_streamed_response(completion)

        print("\n\nFull response assembled:", full_response)

    except Exception as e:
        print(f"An error occurred: {e}")


if __name__ == "__main__":
    main()