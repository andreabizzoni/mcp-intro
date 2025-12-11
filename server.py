from mcp.server.fastmcp import FastMCP
from dotenv import load_dotenv
import os

load_dotenv()

mcp = FastMCP(
    name="Calculator",
    host="0.0.0.0",
    port=8050,
)


@mcp.tool()
def add(a: int, b: int) -> int:
    """Add two numbers together"""
    return a + b


if __name__ == "__main__":
    transport = os.getenv("TRANSPORT")
    if transport == "sse":
        print("Running server with sse transport")
        mcp.run(transport="sse")
    elif transport == "stdio":
        print("Running server with stdio transport")
        mcp.run(transport="stdio")
    else:
        raise ValueError(f"Invalid transport name: {transport}")
