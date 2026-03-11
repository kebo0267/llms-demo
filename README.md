# LLM Demo Cheat Sheet

Quick reference for the tools and libraries used in the demos.

## Demos

| File | What it does | Stack |
|------|-------------|-------|
| `src/ollama_chatbot.py` | Terminal chatbot | Ollama + LangChain |
| `src/gradio_chatbot.py` | Web UI chatbot | Ollama + LangChain + Gradio |
| `src/huggingface_chatbot.py` | Terminal chatbot, no server | HuggingFace Transformers |

---

## Ollama

Local inference server — runs models on your machine behind a REST API.

```bash
# Install
curl -fsSL https://ollama.com/install.sh | sh

# Start the server (runs on localhost:11434)
ollama serve

# Pull a model
ollama pull qwen2.5:3b

# List downloaded models
ollama list

# Run a model interactively
ollama run qwen2.5:3b

# Remove a model
ollama rm qwen2.5:3b
```

### Environment variables

| Variable | Purpose |
|----------|---------|
| `OLLAMA_MODELS` | Directory where models are stored |
| `OLLAMA_HOST` | Server address (default `127.0.0.1:11434`) |

---

## HuggingFace Transformers

Load and run models directly in Python — no server needed.

```python
from transformers import AutoModelForCausalLM, AutoTokenizer

# Load model and tokenizer (downloads on first run)
tokenizer = AutoTokenizer.from_pretrained('Qwen/Qwen2.5-3B-Instruct')
model = AutoModelForCausalLM.from_pretrained('Qwen/Qwen2.5-3B-Instruct')

# Build a prompt using the chat template
messages = [
    {'role': 'system', 'content': 'You are a helpful assistant.'},
    {'role': 'user', 'content': 'Hello!'},
]

text = tokenizer.apply_chat_template(
    messages,
    tokenize=False,
    add_generation_prompt=True,
)

# Tokenize and generate
inputs = tokenizer(text, return_tensors='pt').to(model.device)

output = model.generate(
    **inputs,
    max_new_tokens=512,
    temperature=0.7,
    do_sample=True,
)

# Decode only the new tokens
new_tokens = output[0][inputs['input_ids'].shape[1]:]
print(tokenizer.decode(new_tokens, skip_special_tokens=True))
```

### Environment variables

| Variable | Purpose |
|----------|---------|
| `HF_HOME` | Directory where models/cache are stored |

---

## LangChain

Framework for building LLM applications. Used here for chat message types and the Ollama integration.

```python
from langchain_ollama import ChatOllama
from langchain_core.messages import AIMessage, HumanMessage, SystemMessage

# Create the LLM client (talks to a running Ollama server)
llm = ChatOllama(
    model='qwen2.5:3b',
    temperature=0.7,
)

# Build a conversation as a list of message objects
messages = [
    SystemMessage(content='You are a helpful assistant.'),
    HumanMessage(content='Hello!'),
]

# Get a response
response = llm.invoke(messages)
print(response.content)

# Append the response to history and continue
messages.append(response)  # response is an AIMessage
messages.append(HumanMessage(content='Follow-up question'))
response = llm.invoke(messages)
```

### Key classes

| Class | Purpose |
|-------|---------|
| `ChatOllama` | LLM client that connects to Ollama |
| `SystemMessage` | Sets the model's behavior/persona |
| `HumanMessage` | A user message |
| `AIMessage` | A model response |

---

## Gradio

Build a web UI for a chatbot with a few lines of code.

```python
import gradio as gr

def respond(message, history):
    # message: str — the latest user input
    # history: list of [user, assistant] pairs
    return 'Hello!'  # return the assistant's reply as a string

demo = gr.ChatInterface(
    fn=respond,
    title='My Chatbot',
)

demo.launch()
```

### `gr.ChatInterface`

| Parameter | Purpose |
|-----------|---------|
| `fn` | Response function `(message, history) -> str` |
| `title` | Title shown in the web page |

### `demo.launch()`

| Parameter | Default | Purpose |
|-----------|---------|---------|
| `server_name` | `127.0.0.1` | Bind address (`0.0.0.0` for external access) |
| `server_port` | `7860` | Port number |
| `share` | `False` | Create a public Gradio link |

