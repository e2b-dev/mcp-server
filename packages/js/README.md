# E2B MCP Server (JavaScript)

A Model Context Protocol server for running code in a secure sandbox by [E2B](https://e2b.dev).

## Development

Navigate to the JavaScript package directory:
```bash
cd mcp-server/packages/js
```

Install dependencies:
```
npm install
```

Build the server:
```
npm run build
```

For development with auto-rebuild:
```
npm run watch
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

Note: Make sure you have an E2B API key set up. You can get one from [e2b.dev](https://e2b.dev).

### Troubleshooting

If you encounter dependency issues:
- Ensure you've run `npm install` in the correct directory (`mcp-server/packages/js`)
- Check that all dependencies like `@e2b/code-interpreter` are properly installed
- If building from source, make sure to run `npm run build` before attempting to use the server

### Debugging

Since MCP servers communicate over stdio, debugging can be challenging. We recommend using the [MCP Inspector](https://github.com/modelcontextprotocol/inspector), which is available as a package script:

```
npm run inspector
```

The Inspector will provide a URL to access debugging tools in your browser.
