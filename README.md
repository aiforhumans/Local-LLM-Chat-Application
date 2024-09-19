# Local LLM Chat Application

This Python application demonstrates how to interact with a local Language Model (LLM) using the OpenAI API format. It's designed to work with local LLM servers like those provided by LM Studio.

## Features

- Connects to a local LLM server using the OpenAI API format
- Supports chat completions with streaming responses
- Configurable model parameters
- Error handling for robust operation

## Prerequisites

- Python 3.6+
- OpenAI Python library
- A local LLM server (e.g., LM Studio) running on `http://localhost:1234`

## Installation

1. Clone this repository or download the `app.py` file.
2. Install the required Python package:

   ```
   pip install openai
   ```

## Usage

1. Ensure your local LLM server is running on `http://localhost:1234`.
2. Run the script:

   ```
   python app.py
   ```

3. The script will send a predefined series of messages to the LLM and stream the response.

## Code Overview

- `create_client()`: Sets up the OpenAI client to connect to the local LLM server.
- `prepare_chat_params()`: Prepares the parameters for the chat completion request.
- `process_streamed_response()`: Handles the streaming response from the LLM.
- `main()`: Orchestrates the chat process and error handling.

## Configuration

You can modify the following parameters in the `main()` function:

- `model_name`: The name of the model to use (default: "gpt-3.5-turbo")
- `messages`: The conversation history and prompts sent to the LLM
- Chat parameters in `prepare_chat_params()`: temperature, max_tokens, etc.

## Notes

- This application is designed for use with local LLM servers that implement the OpenAI API format.
- The API key used is a dummy value, as local setups typically don't require authentication.
- Ensure your local LLM server supports the `/v1/chat/completions` endpoint.

## Supported Endpoints

The local LLM server is expected to support the following OpenAI-compatible endpoints:

- GET /v1/models
- POST /v1/chat/completions
- POST /v1/embeddings
- POST /v1/completions

This application specifically uses the chat completions endpoint (`/v1/chat/completions`).

## Error Handling

The application includes basic error handling to catch and display any exceptions that occur during execution.

## Contributing

Feel free to fork this repository and submit pull requests with any enhancements.

## License

[Specify your license here, e.g., MIT, GPL, etc.]
