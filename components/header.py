from selenium.webdriver.common.by import By

from utils import Locator


class Header:
    def __init__(self) -> None:
        self.tarrifs = Locator(By.XPATH, "//a[text()='Тарифы']", "Header:Tarrifs")
        self.contacts = Locator(By.XPATH, "//a[text()='Контакты']", "Header:Contacts")
        self.support = Locator(By.XPATH, "//a[text()='Поддержка']", "Header:Support")
        self.start_work = Locator(By.XPATH, "//span[text()='Начать работу']", "Header:StartWork")

    def verify(self) -> bool:
        self.tarrifs.is_on_page()
        self.contacts.is_on_page()
        self.support.is_on_page()
        self.start_work.is_on_page()
        return True
