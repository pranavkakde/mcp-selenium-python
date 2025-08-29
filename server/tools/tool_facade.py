from tools.mcp_tools import launch_page, enter_text, click, close_browser

class ToolsFacade:
    """Facade that exposes high-level web actions for MCP."""
    async def launch_page(url: str, browser: str, headless: bool = False) -> bool:
        return launch_page(url, browser, headless)
    
    async def enter_text(locator_type: str, locator_value: str, text: str) -> bool:
        return enter_text(locator_type, locator_value, text)
    
    async def click(locator_type: str, locator_value: str) -> bool:
        return click(locator_type, locator_value)
    
    async def close_browser():
        return close_browser()