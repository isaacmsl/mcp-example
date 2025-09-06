# MCP Example

This is a simple example of MCP using Python.
We use a local Ollama LLM model "gemma3:27b".

## Requirements

1. Python 3.11
1. uv

## Usage

1. On `client.py`, you can set the generate URL of your preference.
In addition, set your model.

```py
class MCPClient:
    def __init__(self):
        self.session: Optional[ClientSession] = None
        self.exit_stack = AsyncExitStack()
        self.model = RemoteOllamaModelWithTools(generate_url="http://192.168.170.116:11434/api/generate")
        self.model_name = "gemma3:27b"
```

1. Create a virtual env and activate your venv (command will help you with that):

```bash
uv venv
```

1. Install dependencies:

```bash
uv sync
```

1. Run with server1 (USA Weather API) or server2 (calculator):
```bash
python client.py server1.py
```