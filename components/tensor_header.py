from selenium.webdriver.common.by import By

from utils import Locator


class TensorHeader:
    def __init__(self) -> None:
        self.about = Locator(By.XPATH, "//a[text()='О компании']", "TensorHeader:About")
        self.dev = Locator(By.XPATH, "//a[text()='Разработка ПО']", "TensorHeader:Dev")
        self.vacancies = Locator(By.XPATH, "//a[@href='/vacancies']", "TensorHeader:Vacancies")
        self.contacts = Locator(By.XPATH, "//a[@href='/contacts']", "TensorHeader:Contacts")

    def verify(self) -> bool:
        assert self.about.is_on_page()
        assert self.dev.is_on_page()
        assert self.vacancies.is_on_page()
        assert self.contacts.is_on_page()
        return True

