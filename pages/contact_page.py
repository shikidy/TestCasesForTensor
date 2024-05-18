from selenium.webdriver.common.by import By

from utils import Locator
from utils import Locator
from components.header import Header
from .base_page import BasePage


class ContactPageLocators:
    tensor_banner = Locator(By.XPATH, "//*[@id=\"contacts_clients\"]/div[1]/div/div/div[2]/div/a/img", "ContactPage:TensorBanner")
    region_name = Locator(By.XPATH, "//*[@id=\"container\"]/div[1]/div/div[3]/div[2]/div[1]/div/div[2]/span/span", "ContactPage:ClientRegion")
    partners_banners = Locator(By.CLASS_NAME, "sbisru-Contacts-List__item", "ContactPage:Partners")
    region_panel = Locator(By.CLASS_NAME, "sbis_ru-Region-Panel", "ContactPage:RegionPanel")


class ContactPage(BasePage):
    
    
    def __init__(self) -> None:
        super().__init__()
        self.base_url = "https://sbis.ru/contacts/"
        self.header = Header()
        self.banner = ContactPageLocators.tensor_banner
        self.client_region = ContactPageLocators.region_name
        self.partners = ContactPageLocators.partners_banners
        self.region_panel = ContactPageLocators.region_panel
        

    def _verify_page(self):
        self.header.verify()
        self.banner.is_on_page()
        self.client_region.is_on_page()
        self.partners.is_on_page()

    def switch_region(self, region_title: str):
        
        self.client_region.click_first()
        self.region_panel.is_on_page()

        region_link = Locator(By.XPATH, f"//span[@class='sbis_ru-link' and contains(@title, '{region_title}')]", "ContactPage:SwitchRegionLink")
        region_link.is_on_page()
        region_link.click_first()


    
    