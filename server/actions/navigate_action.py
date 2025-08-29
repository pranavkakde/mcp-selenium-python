from log_writer import logger
from engine import driver_session_manager

class NavigateAction:
    def __init__(self, driver) -> None:
        self.driver = driver
    def launch_page(self, url: str)->bool:
        try:
            self.driver.get(url)
            logger.info(f"Launched page {url}")
            return True
        except Exception as e:
            logger.error(f"Launch failed: {e}")
            return False
