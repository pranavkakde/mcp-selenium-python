from fastmcp import FastMCP
from tools.tool_facade import ToolsFacade
from log_writer import logger
import asyncio, inspect, os


mcp = FastMCP(name="mcp_selenium_server")

# register all async methods from ToolsFacade
for name, method in inspect.getmembers(ToolsFacade, predicate=inspect.iscoroutinefunction):
    logger.info(f"Registering MCP Tool: {name}")
    mcp.tool()(method)

if __name__ == "__main__":
    logger.info(f"MCP server started on port {os.getenv('Port', 8080)}")
    asyncio.run(
        mcp.run_async(
            transport="streamable-http",
            host="0.0.0.0",
            port=os.getenv("PORT", 8080)
        )
    )