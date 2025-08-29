# MCP Selenium Server & Client

This project provides a **Model Context Protocol (MCP) server and client implementation for Selenium-based browser automation**. It allows LLMs or external tools to interact with a browser through a standardized protocol, supporting actions like navigation, input, and clicks.

---

## 🚀 Features
- **MCP Server**: Exposes Selenium browser automation as tools.
- **MCP Client**: Sends tool calls (e.g., navigate, click, input) and receives structured results.
- **Extensible Actions**: Modular design for actions (`navigate`, `click`, `input`). More actions to be added.
- **Driver Management**: Abstraction for Selenium sessions and locator strategies.
- **Tool Facade**: Unified interface for tools (`mcp_tools`, `webtools`).
- **Logging & Context**: Centralized log writer and execution context.

---

## 📂 Project Structure
```
.
├── client/
│   ├── client.py              # MCP client implementation
│   ├── llm_client.py          # Example LLM client integration (currently set to use Gemini)
│
├── server/
│   ├── mcp_selenium_server.py # MCP server entry point
│   ├── custom_context.py      # Execution context handling
│   ├── log_writer.py          # Logging utilities
│   ├── actions/               # Browser actions (navigate, click, input)
│   ├── engine/                # Driver/session/locator management
│   └── tools/                 # Tool definitions (MCP tools, web tools)
│
├── .env                       # Environment variables
├── pyproject.toml             # Project dependencies & configuration
├── uv.lock                    # Dependency lock file
├── LICENSE                    # License file
└── README.md                  # (this file)
```

---

## ⚙️ Installation

1. Clone the repo:
   ```bash
   git clone <repo-url>
   cd mcp-selenium
   ```

2. Install dependencies (using [uv](https://github.com/astral-sh/uv) or poetry):
   ```bash
   uv sync
   ```

3. Set environment variables in `.env` if needed (e.g., LLM API Key).

---

## ▶️ Usage

### Start the MCP Server
```bash
python server/mcp_selenium_server.py
```

### Run the Client
```bash
python client/client.py
```

### Example JSON-RPC Request
```json
{
  "action": "launch_page",
  "args": {
    "url": "https://google.com",
    "browser": "edge",
    "headless": false
  }
}
```

### Example Actions
- `launch_page` → Open a URL
- `click` → Click an element
- `enter_text` → Type text into a field
At present only these actions are added but can be extended for more actions.
---

## 🛠 Development
- Python 3.10+
- Selenium WebDriver
- MCP protocol integration

Lint & format before committing:
```bash
uv run black .
uv run flake8 .
```

---

## 📜 License
This project is licensed under the terms of the [MIT License](LICENSE).

