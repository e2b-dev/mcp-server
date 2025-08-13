"""
Run the E2B MCP server with streamable HTTP transport using the official SDK.
"""

import contextvars
import json
import logging
from collections.abc import Sequence

from dotenv import load_dotenv
from mcp.server.fastmcp import FastMCP
from mcp.server.auth.provider import AccessToken, TokenVerifier
from mcp.server.auth.settings import AuthSettings
from mcp.types import TextContent, ImageContent, EmbeddedResource, Tool
from e2b_code_interpreter import Sandbox
from pydantic import BaseModel, AnyHttpUrl

# Load environment variables
load_dotenv()

# Suppress known harmless errors from MCP SDK streamable HTTP transport
logging.getLogger("mcp.server.streamable_http").setLevel(logging.CRITICAL)

# Store the token for the current request
current_token: contextvars.ContextVar[str | None] = contextvars.ContextVar("current_token", default=None)


# Tool schema (copied from server.py for HTTP version)
class ToolSchema(BaseModel):
    code: str


class E2BTokenVerifier(TokenVerifier):
    """Token verifier that stores the E2B API key for use in tools."""

    async def verify_token(self, token: str) -> AccessToken | None:
        """Verify token and store it for the current request."""
        # Store the token in context for use in tools
        current_token.set(token)
        
        # Return a valid access token - we don't validate, just pass through
        return AccessToken(
            token=token,
            scopes=["e2b"],  # Dummy scope
            client_id="e2b-mcp-client",  # Required field
        )


# Create FastMCP server instance with token verifier and auth settings
mcp = FastMCP(
    "e2b-mcp-server",
    stateless_http=True,
    json_response=True,
    token_verifier=E2BTokenVerifier(),
    auth=AuthSettings(
        issuer_url=AnyHttpUrl("https://e2b.dev"),  # E2B as issuer
        resource_server_url=AnyHttpUrl("http://localhost:8000"),  # This server's URL
        required_scopes=["e2b"],
    ),
)


# FastMCP automatically exposes tools/list based on registered @mcp.tool() functions
# No need for custom list_tools function - authentication is handled by token_verifier


@mcp.tool()
async def run_code(code: str) -> Sequence[TextContent | ImageContent | EmbeddedResource]:
    """Run python code in a secure sandbox by E2B. Using the Jupyter Notebook syntax."""
    # Get the token from the current request context - mandatory for HTTP mode
    api_key = current_token.get()
    if not api_key:
        raise ValueError("Authorization header with Bearer token is required")
    
    sandbox = Sandbox(api_key=api_key)
    execution = sandbox.run_code(code)
    
    result = {
        "stdout": execution.logs.stdout,
        "stderr": execution.logs.stderr,
    }
    
    return [
        TextContent(
            type="text",
            text=json.dumps(result, indent=2)
        )
    ]


def main() -> None:
    """Run server with streamable HTTP transport."""
    mcp.run(transport="streamable-http")


if __name__ == "__main__":
    main()


