from actions.base_action import BaseAction
from selenium.common.exceptions import TimeoutException, NoSuchElementException
from log_writer import logger
from selenium.webdriver.common.action_chains import ActionChains

class ClickAction(BaseAction):
    def click(self, locator_type: str, locator_value: str):
        try:
            element = self._wait_for_clickable(locator_type, locator_value)
            element.click()
            logger.info(f"Clicked {locator_type}={locator_value}")
            return True
        except TimeoutException:
            logger.error(f"Timeout: Element not clickable ({locator_type}={locator_value})")
            return False
        except Exception as e:
            logger.error(f"Click failed {e}")
            return False
    
    def double_click(self, locator_type: str, locator_value: str):
        try:
            element = self._wait_for_clickable(locator_type, locator_value)
            actionchains = ActionChains(self.driver)
            actionchains.double_click(locator_value).perform()
            logger.info(f"Clicked {locator_type}={locator_value}")
            return True
        except TimeoutException:
            logger.error(f"Timeout: Element not clickable ({locator_type}={locator_value})")
            return False
        except Exception as e:
            logger.error(f"Click failed {e}")
            return False