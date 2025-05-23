# E2B MCP Server (JavaScript)

A Model Context Protocol server for running code in a secure sandbox by [E2B](https://e2b.dev).

## Development

Install dependencies:
```
pnpm install
```

Build the server:
```
pnpm build
```

For development with auto-rebuild:
```
pnpm watch
```

## Installation

To use with Claude Desktop, add the server config:

On MacOS: `~/Library/Application Support/Claude/claude_desktop_config.json`
On Windows: `%APPDATA%/Claude/claude_desktop_config.json`

```json
{
  "mcpServers": {
    "e2b-server": {
      "command": "npx",
      "args": ["-y", "@e2b/mcp-server"],
      "env": { "E2B_API_KEY": "${e2bApiKey}" }
    }
  }
}
```

### Debugging

Since MCP servers communicate over stdio, debugging can be challenging. We recommend using the [MCP Inspector](https://github.com/modelcontextprotocol/inspector), which is available as a package script:

```
pnpm inspector
```

The Inspector will provide a URL to access debugging tools in your browser.
