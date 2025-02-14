# E2B MCP Server (Python)

A Model Context Protocol server for running code in a secure sandbox by [E2B](https://e2b.dev).

<a href="https://glama.ai/mcp/servers/o9swvhmy2i"><img width="380" height="200" src="https://glama.ai/mcp/servers/o9swvhmy2i/badge" alt="e2b-mcp-server MCP server" /></a>

## Development

Install dependencies:
```
uv install
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

Since MCP servers communicate over stdio, debugging can be challenging. We recommend using the [MCP Inspector](https://github.com/modelcontextprotocol/inspector), which is available as a package script:

```
npx @modelcontextprotocol/inspector \
  uv \
  --directory . \
  run \
  e2b-mcp-server \
```

The Inspector will provide a URL to access debugging tools in your browser.
