from dataclasses import dataclass

import allure
import pytest

from pages.main_page import MainPage
from pages.contact_page import ContactPage


@dataclass
class RegionTestData:
    region_to_check: str
    region_to_switch: str
    region_to_switch_path: str

def main_page():
    main_page = MainPage()
    main_page.open()
    main_page.verify_page()
    main_page.header.contacts.click_first()


def contact_page(
        region_to_check: str,  
        region_to_switch: str, 
        region_to_switch_path: str
        ):
    contact_page = ContactPage()
    contact_page.verify_page()
    
    with allure.step("Checking client region"):
        assert contact_page.client_region.text == region_to_check

    with allure.step("Checking no empty partners"):
        assert len(contact_page.partners.elements)
        partners_list = contact_page.partners.elements

    with allure.step(f"Switching region to {region_to_switch}"):
        old_url = contact_page.full_url
        contact_page.switch_region(region_to_switch)
        contact_page.wait_unit_redirect(old_url)
        contact_page.verify_page()

    with allure.step("Checking no empty partners"):
        assert len(contact_page.partners.elements)

    with allure.step("Checking partners changed"):
        assert contact_page.partners.elements != partners_list

    with allure.step("Checking url path for new region"):
        assert region_to_switch_path in contact_page.full_url

    with allure.step("Checking page title for new region"):
        assert region_to_switch in contact_page.page_title
    
@allure.story("Second test script")
@pytest.mark.parametrize(
    "test_data", [
        RegionTestData("Новосибирская обл.", "Камчатский край", "41-kamchatskij-kraj")
    ]
)

def test_second_script(test_data: RegionTestData):
    with allure.step("Main page"):
        main_page()

    with allure.step("Contact page"):
        contact_page(
            test_data.region_to_check, 
            test_data.region_to_switch, 
            test_data.region_to_switch_path
        )