from utils import Locator

from selenium.webdriver.common.by import By

from components.tensor_header import TensorHeader
from .base_page import BasePage


class TensorAboutPageLocators:
    work_images = Locator(By.CLASS_NAME, "tensor_ru-About__block3-image", "TensorAbout:WorkImages" )


class TensorAboutPage(BasePage):
    
    
    def __init__(self) -> None:
        super().__init__()
        self.base_url = "https://tensor.ru/about"
        self.header = TensorHeader()
        self.work_images = TensorAboutPageLocators.work_images

    def _verify_page(self):
        assert self.header.verify()
        assert self.work_images.is_on_page()
    