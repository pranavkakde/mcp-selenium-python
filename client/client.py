import asyncio
from fastmcp import Client

# ---------- set server endpoint -------------
MCP_SERVER_URL = "http://localhost:8080/mcp"

# -----------Test method ----------------
async def test_mcp_server():
    async with Client(MCP_SERVER_URL) as client:
        tools = await client.list_tools()
        for tool in tools:
            print(f" Tool Found: {tool.name}")
        
        print(f"Calling launch page for edge browser with url http://google.com")
        result = await client.call_tool("launch_page",{"url": "https://www.google.com", "browser": "edge", "headless": False})
        print(f"Result: {result}")

        print(f"Calling enter_text tool")
        result = await client.call_tool("enter_text", {"locator_type":"name", "locator_value": "q", "text": "python mcp"})
        print(f"Result: {result}")

        print(f"Calling click tool")
        result = await client.call_tool("click",  {"locator_type":"name", "locator_value": "btnK"})
        print(f"Result: {result}")

        print(f"Calling close_browser tool")
        result = await client.call_tool("close_browser", {})
        print(f"Result: {result}")

# --------- main entry -------------
if __name__ == "__main__":
    asyncio.run(test_mcp_server())