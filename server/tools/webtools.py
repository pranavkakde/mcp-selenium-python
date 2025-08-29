from actions.click_action import ClickAction
from actions.input_action import InputAction
from actions.navigate_action import NavigateAction

class WebTools:
    def __init__(self, driver) -> None:
        self.clicker = ClickAction(driver)
        self.inputtter = InputAction(driver)
        self.navigator = NavigateAction(driver)

    def click(self, locator_type: str, locator_value: str):
        return self.clicker.click(locator_type, locator_value)
    
    def enter_text(self, locator_type: str, locator_value: str, text: str):
        return self.inputtter.enter_text(locator_type, locator_value, text)
    
    def launch_page(self, url: str):
        return self.navigator.launch_page(url)