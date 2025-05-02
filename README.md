![E2B MCP Server Preview Light](/readme-assets/mcp-server-light.png#gh-light-mode-only)
![E2B MCP Server Preview Dark](/readme-assets/mcp-server-dark.png#gh-dark-mode-only)

# E2B MCP Server

[![smithery badge](https://smithery.ai/badge/e2b)](https://smithery.ai/server/e2b)

This repository contains the source code for the [E2B](https://e2b.dev) MCP server.

The E2B MCP server allows you to add [code interpreting capabilities](https://github.com/e2b-dev/code-interpreter) to your Claude Desktop app via the E2B Sandbox. See demo [here](https://x.com/mishushakov/status/1863286108433317958).


Available in two editions:

- [JavaScript](packages/js/README.md)

- [Python](packages/python/README.md)


### Installing via Smithery

You can also install E2B for Claude Desktop automatically via [Smithery](https://smithery.ai/server/e2b):

```bash
npx @smithery/cli install e2b --client claude
```


## Running evals

The evals package loads an mcp client that then runs the index.ts file, so there is no need to rebuild between tests. You can load environment variables by prefixing the npx command. Full documentation can be found [here](https://www.mcpevals.io/docs).

```bash
OPENAI_API_KEY=your-key  npx mcp-eval evals.ts packages/js/src/index.ts
```