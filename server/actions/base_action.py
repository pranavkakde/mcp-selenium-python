from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, NoSuchElementException

from engine.locator_strategy import LocatorStrategy
from log_writer import logger

class BaseAction:
    def __init__(self, driver, timeout: int = 10):
        self.driver = driver
        self.timeout = timeout
    
    def _wait_for(self, locator_type: str, locator_value: str, condition):
        by_strategy = LocatorStrategy.resolve(locator_type)
        wait = WebDriverWait(self.driver, self.timeout, poll_frequency=1, ignored_exceptions=[NoSuchElementException])
        try:
            return wait.until(condition((by_strategy, locator_value)))
        except TimeoutException:
            logger.error(f"Timeout while waiting for element: {locator_type}")
            raise TimeoutException(f"Timeout while waiting for element: {locator_type}")
        except Exception as e:
            logger.error(f"Exception in wait for {e}")
            raise
    
    def _wait_for_element(self, locator_type: str, locator_value: str):
        return self._wait_for(locator_type, locator_value, EC.presence_of_element_located)
    
    def _wait_for_clickable(self, locator_type: str, locator_value: str):
        return self._wait_for(locator_type, locator_value, EC.element_to_be_clickable)