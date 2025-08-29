from engine.driver_session_manager import DriverSessionManager
from log_writer import logger
from tools.webtools import WebTools

driver_session_manager = DriverSessionManager()

def tool_action(func):
    """Decorator to wrap tool calls with driver setup, logging and error handling"""
    def wrapper(*args, **kwargs):
        try:
            driver = driver_session_manager.get_driver_session()
            tools = WebTools(driver)
            return func(tools, *args, **kwargs)
        except Exception as e:
            logger.error(f"Exception in {func.__name__}: {e}")
            return False
    return wrapper

def launch_page(url: str, browser: str, headless: bool = False) -> bool:
    """Use this to launch a web page.
    
    Args:
        url: The URL of the site to launch.
        browser: browser name to launch.
        headless: True | False launch browser in headless mode.
    
    Returns:
        True if the url is launched.
    """
    try:
        driver = driver_session_manager.create_driver_session(browser, headless)
        tools = WebTools(driver)
        tools.launch_page(url)
        logger.info(f"Tool: Launched Browser with {url}")
        return True
    except Exception as e:
        logger.error(f"Exception in launching url {e}")
        return False

@tool_action
def enter_text(tools: WebTools, locator_type: str, locator_value: str, text: str) -> bool:
    """Use this to enter text in a text box

    Args:
        locator_type: Locator Type of the web element.
                    e.g. ["id", "name", "xpath"]
        locator_value: Value of the locator based on its type.
        value: The value to write to the text box.

    Returns:
        True if the value is written successfully.         
    """
    try:
        tools.enter_text(locator_type, locator_value, text)
        logger.info(f"Tool: enter_text called with {locator_type}: {locator_value}, value {text}")
        return True
    except Exception as e:
        logger.error(f"Exception in enter_text {e}")
        return False

@tool_action
def click(tools: WebTools, locator_type: str, locator_value: str) -> bool:
    """Use this to click on an object by name.

    Args:
        locator_type: Locator Type of the web element.
                    e.g. ["id", "name", "xpath"]
        locator_value: Value of the locator based on its type.

    Returns:
        True if the value is clicked successfully.
    """
    try:
        tools.click(locator_type, locator_value)
        logger.info(f"Tool: click called with {locator_type}: {locator_value}")
        return True
    except Exception as e:
        logger.error(f"exception in click {e}")
        return False

def close_browser():
    """Use this to close a webdriver session.

    Args: 

    Returns:
        True if webdriver closed successfully.
    """
    try:
        driver_session_manager.close_driver_session()
        logger.info(f"Tool: close_browser called")
        return True
    except Exception as e:
        logger.error(f"exception in close_browser {e}")
        return False

def close_all_browsers() -> bool:
    """Close all browser sessions"""
    try:
        driver_session_manager.close_all_sessions()
        logger.info(f"Tool: close_all_browsers called")
        return True
    except Exception as e:
        logger.error(f"Exception in close_all_browsers: {e}")
        return False