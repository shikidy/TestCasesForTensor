from utils import Locator

from selenium.webdriver.common.by import By

from components.header import Header
from utils import Locator
from .base_page import BasePage


class MainPageLocators:
    download_local_versions = Locator(By.XPATH, "//a[text()='Скачать локальные версии' and @class='sbisru-Footer__link']", "MainPage:DownloadLocalVers")


class MainPage(BasePage):
    
    
    def __init__(self) -> None:
        super().__init__()
        self.header = Header()
        self.download_local_ver = MainPageLocators.download_local_versions

    def _verify_page(self):
        self.header.verify()
        self.download_local_ver.is_on_page()

 
    