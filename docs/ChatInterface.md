from __future__ import annotations
ChatInterface is Gradio's high-level abstraction for creating chatbot UIs, and allows you to create a web-based demo around a chatbot model in a few lines of code. Only one parameter is required: fn, which takes a function that governs the response of the chatbot based on the user input and chat history. Additional parameters can be used to control the appearance and behavior of the demo.

from typing import Callable, List, Union
from gradio.blocks import Blocks
from gradio.components import Component, MultimodalTextbox, Textbox
from gradio.interface import Interface
from gradio.themes import Theme

ChatInterfaceInitParams = dict[
    fn: Callable[[str, List[List[str]]], str],
    multimodal: bool,
    type: Literal['messages', 'tuples'],
    chatbot: Chatbot | None,
    textbox: Textbox | MultimodalTextbox | None,
    additional_inputs: List[Component | str] | None,
    additional_inputs_accordion_name: str | None,
    additional_inputs_accordion: str | Accordion | None,
    examples: List[str] | List[dict[str, str | List]] | List[List] | None,
    cache_examples: bool | Literal['lazy'] | None,
    examples_per_page: int,
    title: str | None,
    description: str | None,
    theme: Theme | str | None,
    css: str | None,
    js: str | None,
    head: str | None,
    analytics_enabled: bool | None,
    submit_btn: str | None | Button,
    stop_btn: str | None | Button,
    retry_btn: str | None | Button,
    undo_btn: str | None | Button,
    clear_btn: str | None | Button,
    autofocus: bool,
    concurrency_limit: int | None | Literal['default'],
    fill_height: bool,
    delete_cache: tuple[int, int] | None,
    show_progress: Literal['full', 'minimal', 'hidden'],
    fill_width: bool,
]
Initialization
Parameters
▼
fn: Callable
the function to wrap the chat interface around. Should accept two parameters: a string input message and list of two-element lists of the form [[user_message, bot_message], ...] representing the chat history, and return a string response. See the Chatbot documentation for more information on the chat history format.

def ChatInterface(
    fn: Callable[[str, List[List[str]]], str],
    **kwargs: ChatInterfaceInitParams
) -> Interface:
    """
    ChatInterface is Gradio's high-level abstraction for creating chatbot UIs, and allows you to create a web-based demo around a chatbot model in a few lines of code. Only one parameter is required: fn, which takes a function that governs the response of the chatbot based on the user input and chat history. Additional parameters can be used to control the appearance and behavior of the demo.
multimodal: bool
default = False
if True, the chat interface will use a gr.MultimodalTextbox component for the input, which allows for the uploading of multimedia files. If False, the chat interface will use a gr.Textbox component for the input.

    Parameters
    ----------
    fn : Callable[[str, List[List[str]]], str]
        the function to wrap the chat interface around. Should accept two parameters: a string input message and list of two-element lists of the form [[user_message, bot_message], ...] representing the chat history, and return a string response. See the Chatbot documentation for more information on the chat history format.
type: Literal['messages', 'tuples']
default = "tuples"
chatbot: Chatbot | None
default = None
an instance of the gr.Chatbot component to use for the chat interface, if you would like to customize the chatbot properties. If not provided, a default gr.Chatbot component will be created.

    Returns
    -------
    Interface
        an instance of the Interface class, which can be launched with the `launch()` method.
    """
    blocks = Blocks()
    blocks.chatbot(fn, **kwargs)
    return Interface(blocks, **kwargs)
textbox: Textbox | MultimodalTextbox | None
default = None
an instance of the gr.Textbox or gr.MultimodalTextbox component to use for the chat interface, if you would like to customize the textbox properties. If not provided, a default gr.Textbox or gr.MultimodalTextbox component will be created.

additional_inputs: str | Component | list[str | Component] | None
default = None
an instance or list of instances of gradio components (or their string shortcuts) to use as additional inputs to the chatbot. If components are not already rendered in a surrounding Blocks, then the components will be displayed under the chatbot, in an accordion.

additional_inputs_accordion_name: str | None
default = None
Deprecated. Will be removed in a future version of Gradio. Use the `additional_inputs_accordion` parameter instead.

additional_inputs_accordion: str | Accordion | None
default = None
if a string is provided, this is the label of the `gr.Accordion` to use to contain additional inputs. A `gr.Accordion` object can be provided as well to configure other properties of the container holding the additional inputs. Defaults to a `gr.Accordion(label="Additional Inputs", open=False)`. This parameter is only used if `additional_inputs` is provided.

examples: list[str] | list[dict[str, str | list]] | list[list] | None
default = None
sample inputs for the function; if provided, appear below the chatbot and can be clicked to populate the chatbot input. Should be a list of strings if `multimodal` is False, and a list of dictionaries (with keys `text` and `files`) if `multimodal` is True.

cache_examples: bool | Literal['lazy'] | None
default = None
if True, caches examples in the server for fast runtime in examples. The default option in HuggingFace Spaces is True. The default option elsewhere is False.

examples_per_page: int
default = 10
if examples are provided, how many to display per page.

title: str | None
default = None
a title for the interface; if provided, appears above chatbot in large font. Also used as the tab title when opened in a browser window.

description: str | None
default = None
a description for the interface; if provided, appears above the chatbot and beneath the title in regular font. Accepts Markdown and HTML content.

theme: Theme | str | None
default = None
a Theme object or a string representing a theme. If a string, will look for a built-in theme with that name (e.g. "soft" or "default"), or will attempt to load a theme from the Hugging Face Hub (e.g. "gradio/monochrome"). If None, will use the Default theme.

css: str | None
default = None
custom css as a string or path to a css file. This css will be included in the demo webpage.

js: str | None
default = None
custom js as a string or path to a js file. The custom js should be in the form of a single js function. This function will automatically be executed when the page loads. For more flexibility, use the head parameter to insert js inside <script> tags.

head: str | None
default = None
custom html to insert into the head of the demo webpage. This can be used to add custom meta tags, multiple scripts, stylesheets, etc. to the page.

analytics_enabled: bool | None
default = None
whether to allow basic telemetry. If None, will use GRADIO_ANALYTICS_ENABLED environment variable if defined, or default to True.

submit_btn: str | None | Button
default = "Submit"
text to display on the submit button. If None, no button will be displayed. If a Button object, that button will be used.

stop_btn: str | None | Button
default = "Stop"
text to display on the stop button, which replaces the submit_btn when the submit_btn or retry_btn is clicked and response is streaming. Clicking on the stop_btn will halt the chatbot response. If set to None, stop button functionality does not appear in the chatbot. If a Button object, that button will be used as the stop button.

retry_btn: str | None | Button
default = "🔄 Retry"
text to display on the retry button. If None, no button will be displayed. If a Button object, that button will be used.

undo_btn: str | None | Button
default = "↩️ Undo"
text to display on the delete last button. If None, no button will be displayed. If a Button object, that button will be used.

clear_btn: str | None | Button
default = "🗑️ Clear"
text to display on the clear button. If None, no button will be displayed. If a Button object, that button will be used.

autofocus: bool
default = True
if True, autofocuses to the textbox when the page loads.

concurrency_limit: int | None | Literal['default']
default = "default"
if set, this is the maximum number of chatbot submissions that can be running simultaneously. Can be set to None to mean no limit (any number of chatbot submissions can be running simultaneously). Set to "default" to use the default concurrency limit (defined by the `default_concurrency_limit` parameter in `.queue()`, which is 1 by default).

fill_height: bool
default = True
if True, the chat interface will expand to the height of window.

delete_cache: tuple[int, int] | None
default = None
a tuple corresponding [frequency, age] both expressed in number of seconds. Every `frequency` seconds, the temporary files created by this Blocks instance will be deleted if more than `age` seconds have passed since the file was created. For example, setting this to (86400, 86400) will delete temporary files every day. The cache will be deleted entirely when the server restarts. If None, no cache deletion will occur.

show_progress: Literal['full', 'minimal', 'hidden']
default = "minimal"
how to show the progress animation while event is running: "full" shows a spinner which covers the output component area as well as a runtime display in the upper right corner, "minimal" only shows the runtime display, "hidden" shows no progress animation at all

fill_width: bool
default = False
Whether to horizontally expand to fill container fully. If False, centers and constrains app to a maximum width.

Demos

