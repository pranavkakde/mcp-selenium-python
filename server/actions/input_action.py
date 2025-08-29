from actions.base_action import BaseAction
from log_writer import logger

class InputAction(BaseAction):
    def enter_text(self, locator_type: str, locator_value: str, text: str):
        try:
            element = self._wait_for_element(locator_type, locator_value)
            element.clear()
            element.send_keys(text)
            logger.info(f"Entered text in {locator_type}={locator_value}")
            return True
        except Exception as e:
            logger.error(f"Enter text failed: {e}")
            return False