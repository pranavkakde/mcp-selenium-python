from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.edge.service import Service as EdgeService
from selenium.webdriver.firefox.service import Service as FirefoxService

class WebDriverFactory():
    """
    WebDriver factory class to create the driver instance.
    """
    @staticmethod
    def create_driver(browser: str = "chrome", headless: bool = False):
        """create driver instance based on the browser name and headless mode
        Args:
            browser (str): browser name
            headless (bool): headless mode
        Returns:
            webdriver: driver instance
        """
        browser = browser.lower()
        if browser == "chrome":
            options = webdriver.ChromeOptions()
            if headless:
                options.add_argument("--headless")
            driver = webdriver.Chrome(service=ChromeService(), options=options)
        elif browser == "edge":
            options = webdriver.EdgeOptions()
            if headless:
                options.add_argument("--headless=new")
            driver = webdriver.Edge(service=EdgeService(), options=options)
        elif browser == "firefox":
            options = webdriver.FirefoxOptions()
            if headless:
                options.add_argument("--headless")
            driver = webdriver.Firefox(service=FirefoxService(), options=options)
        else:
            raise ValueError(f"Invalid browser: {browser}")
        return driver