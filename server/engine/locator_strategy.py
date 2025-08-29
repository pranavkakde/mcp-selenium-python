from selenium.webdriver.common.by import By

class LocatorStrategy():
    _strategies = {
        "id": By.ID,
        "class_name": By.CLASS_NAME,
        "name": By.NAME,
        "tag_name": By.TAG_NAME,
        "link_text": By.LINK_TEXT,
        "partial_link_text": By.PARTIAL_LINK_TEXT,
        "xpath": By.XPATH,
    }

    @classmethod
    def resolve(cls, locator_type: str) -> By:
        """resolve the locator strategy based on the locator string
        Args:
            locator (str): locator string
        Returns:
            By: locator strategy
        """
        if locator_type not in cls._strategies:
            raise ValueError(f"Unsupported locator type: {locator_type}")
        return cls._strategies[locator_type]
