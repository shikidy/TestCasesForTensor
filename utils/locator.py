from __future__ import annotations

from typing import Set, List
from dataclasses import dataclass

import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.common.exceptions import ElementClickInterceptedException

from utils import Driver


class Locator:
    

    def __init__(self, by: By, value: str, name: str) -> None:
        self.__by: By = by
        self.__value = value
        self.__elements: List[WebElement] = None
        self.name = name

    def is_on_page(self, timeout=5) -> bool:
        with allure.step(f"Searching for {self.name}"):
            self.__elements = WebDriverWait(Driver(), timeout)\
                .until(
                    EC.presence_of_all_elements_located((self.__by, self.__value)),
                    message=f"Can't locate element {self.name}"
                    )
        
        return bool(self.__elements)
    
    def click_first(self):
        with allure.step(f"Clicking on first element of {self.name}"):
            Driver().execute_script("arguments[0].click();", self.__elements[0])

            
    
    @property
    def elements(self) -> List[WebElement]:
        return self.__elements
    
    @property
    def text(self) -> str:
        return self.__elements[0].text

    @property
    def href(self) -> str:
        return self.__elements[0].get_attribute("href")


    @staticmethod
    def from_set(data: Set[By, str]) -> Locator:
        return Locator(*data)
