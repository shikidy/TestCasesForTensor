import re
import time
import glob
import os
from typing import List

import allure
from selenium.webdriver.common.by import By

from utils import Locator
from .base_page import BasePage


class DownloadPageLocators:
    download_plugin = Locator(By.XPATH, "//div[text()='СБИС Плагин']", "DownloadPage:DownloadPLuging")
    web_installer = Locator(By.XPATH, "//a[contains(@href, 'Plugin')]", "DownloadPage:DownloadWebInstaller")

class DownloadPage(BasePage):

    def __init__(self) -> None:
        super().__init__()
        self.base_url = "https://sbis.ru/download"

        self.download_plugin = DownloadPageLocators.download_plugin
        self.web_installer = DownloadPageLocators.web_installer

    def _verify_page(self) -> bool:
        self.download_plugin.is_on_page()

    def get_files_by_ext(self, exts: List[str]=["tmp", "crdownload"]) -> List[str]:
        results = []
        for ext in exts:
            results += glob.glob("temp_files/*." + ext)
        return results
    
    def download_web(self):
        with allure.step("Downloading file"):
            self.web_installer.is_on_page()
            self.web_installer.click_first()
            tmp_files = self.get_files_by_ext()
            while tmp_files:
                time.sleep(0.02)
                tmp_files = self.get_files_by_ext()
            time.sleep(0.02)

    def get_exe_size_mb(self) -> int:
        exe_pathes = self.get_files_by_ext(["exe"])
        assert exe_pathes

        return round(os.path.getsize(exe_pathes[0]) / 1024 / 1024, 2)

    def fetch_download_size(self) -> float:
        regular = r"\d+.\d+"
        return float(re.search(regular, self.web_installer.text).group())

    

