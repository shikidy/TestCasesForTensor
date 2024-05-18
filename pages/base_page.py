from typing import List

import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

from utils import Driver, Locator


class BasePage:


    def __init__(self) -> None:
        self.base_url = "https://sbis.ru/"
        self.page_url = "https://sbis.ru/"


    def find_element(self, by: By, value: str, timeout: int=10) -> None:
        return WebDriverWait(Driver(), timeout)\
            .until(
                EC.presence_of_element_located((by, value)),
                message=f"Can't locate element by {(by, value)}"
                )
    
    def find_elements(self, by: By, value: str, timeout: int=10) -> None:
        return WebDriverWait(Driver(), timeout)\
            .until(
                EC.presence_of_all_elements_located((by, value)),
                message=f"Can't locate elements by {(by, value)}"
                )
    
    def open(self):
        Driver().get(self.base_url)
    
    def _verify_page(self) -> bool:
        ...

    def verify_page(self):
        with allure.step("Verify page"):
            self._verify_page()
        
    def set_focus_last_page(self):
        last_page = Driver().window_handles[-1]
        Driver().switch_to.window(last_page)

    def verify_url(self) -> bool:
        return Driver().current_url == self.page_url

    def wait_unit_redirect(self, old_link: str, timeout=5):
        with allure.step(f"Waiting until url change: {old_link}"):
            WebDriverWait(Driver(), timeout)\
                .until(
                    lambda driver: driver.current_url != old_link,
                    message=f"Url didnt update"
                    )
            
    @property
    def full_url(self) -> str:
        return Driver().current_url
        
    @property
    def page_title(self) -> str:
        return Driver().title
    


    

    