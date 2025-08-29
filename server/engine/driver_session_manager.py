from custom_context import CustomContext
from engine.webdriver_factory import WebDriverFactory
from log_writer import logger

class DriverSessionManager():
    """
    Driver session manager class to manage the driver session.
    """
    def __init__(self):
        self.context = CustomContext()

    def get_browser_name(self) -> str:
        return self.context.get_context("browser_name")

    def create_driver_session(self, browser: str = "chrome", headless: bool = False):
        """
        """
        try:
            driver = WebDriverFactory.create_driver(browser, headless)
            self.context.set_context("browser_name", browser)
            self.context.set_context(browser, driver)
            logger.info(f"Webdriver Created: browser = {browser}, headless = {headless}")
        except Exception as e:
            logger.error(f"Error creating driver session: {e}")
            raise RuntimeError(f"Driver Initialization failed for {browser}") from e
        return driver

    def get_driver_session(self):
        """
        """
        try:
            browser_name = self.get_browser_name()
            driver = self.context.get_context(browser_name)
            if driver is None:
                driver = self.create_driver_session(browser_name, False)
                self.context.set_context(browser_name, driver)
        except Exception as e:
            logger.error(f"Exception in retriving driver session {e}")
        return driver

    def close_driver_session(self):
        """"""
        try:
            browser_name = self.get_browser_name()
            driver = self.context.get_context(browser_name)
            if driver:
                driver.quit()
                self.context.set_context(browser_name, None)
                logger.info(f"WebDriver closed for browser = {browser_name}")
        except Exception as e:
            logger.error(f"Exception in closing browser session {e}")
    
    def close_all_sessions(self):
        """"""
        sessions = self.context.get_all_context()
        for session_id, driver in sessions.items():
            if driver:
                try:
                    driver.quit()
                except Exception as e:
                    logger.warning(f"Error closing session {session_id}: {e}")
        self.context.clear_all()
        logger.info("All WebDriver sessions are closed")