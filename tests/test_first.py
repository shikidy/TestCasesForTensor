import allure

from pages.main_page import MainPage
from pages.contact_page import ContactPage
from pages.tensor_page import TensorMainPage
from pages.tensor_about_page import TensorAboutPage


def main_page():
    main_page = MainPage()
    main_page.open()
    main_page.verify_page()
    main_page.header.contacts.click_first()

def contact_page():
    contact_page = ContactPage()
    contact_page.verify_page()
    contact_page.banner.click_first()
    contact_page.set_focus_last_page()

def tensor_main_page():
    tensor_main_page = TensorMainPage()
    tensor_main_page.verify_page()
    tensor_main_page.motivation_banner_link.click_first()

def tensor_about_page():
    tensor_about_page = TensorAboutPage()
    tensor_about_page.verify_page()
    
    first_element = tensor_about_page.work_images.elements[0]

    for image in tensor_about_page.work_images.elements[1:]:
        with allure.step("Checking images size"):
            assert image.size["width"] == first_element.size["width"]
            assert image.size["height"] == first_element.size["height"]
        

@allure.story("First test script")
def test_first_script():
    with allure.step("Main page"):
        main_page()

    with allure.step("Contact page"):
        contact_page()
    
    with allure.step("Tensor main page"):
        tensor_main_page()

    with allure.step("Tensor about page"):
        tensor_about_page()



