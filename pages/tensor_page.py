from utils import Locator

from selenium.webdriver.common.by import By

from components.tensor_header import TensorHeader
from .base_page import BasePage


class TensorMainPageLocators:
    motivation_banner_title = Locator(By.XPATH, "//p[text()='Сила в людях']", "Tensor:MotivationBannerTitle")
    motivation_banner_link = Locator(By.XPATH, "//a[text()='Подробнее' and @href='/about' and @class='tensor_ru-link tensor_ru-Index__link']", "Tensor:MotivationBannerLink" )


class TensorMainPage(BasePage):
    
    
    def __init__(self) -> None:
        super().__init__()
        self.base_url = "https://tensor.ru/"
        self.header = TensorHeader()
        self.motivation_banner_title = TensorMainPageLocators.motivation_banner_title
        self.motivation_banner_link = TensorMainPageLocators.motivation_banner_link

    def _verify_page(self):
        assert self.header.verify()
        assert self.motivation_banner_title.is_on_page()
        assert self.motivation_banner_link.is_on_page()
    