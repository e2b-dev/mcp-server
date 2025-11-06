# E2B MCP Server (Python)

A Model Context Protocol server for running code in a secure sandbox by [E2B](https://e2b.dev).

## Development

Install dependencies with Poetry:
```
cd packages/python
poetry install
```

Or install directly with pip (from project root):
```
python3 -m venv .venv
source .venv/bin/activate
python -m pip install --upgrade pip
cd packages/python
python -m pip install --force-reinstall .
```

## Installation

To use with Claude Desktop, add the server config:

On MacOS: `~/Library/Application Support/Claude/claude_desktop_config.json`
On Windows: `%APPDATA%/Claude/claude_desktop_config.json`

```json
{
  "mcpServers": {
    "e2b-mcp-server": {
      "command": "uvx",
      "args": ["e2b-mcp-server"],
      "env": { "E2B_API_KEY": "${e2bApiKey}" }
    }
  }
}
```

### Debugging

Since MCP servers communicate over stdio, debugging can be challenging. We recommend using the [MCP Inspector](https://github.com/modelcontextprotocol/inspector). You can point it at the Poetry command directly, for example:

```
cd packages/python
npx @modelcontextprotocol/inspector -- poetry run e2b-mcp-server
```

The Inspector will provide a URL to access debugging tools in your browser.

## HTTP Server (Official SDK - Stateless)

Uses the official MCP Python SDK's stateless HTTP transport (no session persistence, no SSE stream).

### Run (HTTP)

With Poetry:
```
cd packages/python
poetry run e2b-mcp-server-http
```

With pip (after following development setup above):
```
e2b-mcp-server-http
```

### Authentication

The server requires an `Authorization: Bearer <E2B_API_KEY>` header for all requests. The token is passed through to the E2B SDK for sandbox operations.

### Examples

The server endpoints and behavior are managed by the official MCP SDK. Check the server logs for the actual URL when it starts.

List tools:

```
curl -s \
  -H "Authorization: Bearer YOUR_E2B_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"jsonrpc":"2.0","id":1,"method":"tools/list","params":{}}' \
  http://localhost:8000/mcp
```

Call tool:

```
curl -s \
  -H "Authorization: Bearer YOUR_E2B_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"jsonrpc":"2.0","id":2,"method":"tools/call","params":{"name":"run_code","arguments":{"code":"print(\"hello world\")"}}}' \
  http://localhost:8000/mcp
```

The server runs in stateless mode with regular JSON responses (no SSE streaming). The actual host, port, and mount path are determined by the SDK's HTTP transport configuration.
