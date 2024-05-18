import allure

from pages.main_page import MainPage
from pages.download_page import DownloadPage


def main_page():
    page = MainPage()
    page.open()
    page.verify_page()
    page.download_local_ver.click_first()

def download_page():
    page = DownloadPage()
    page.wait_unit_redirect(page.base_url)
    page.verify_page()
    old_link = page.full_url
    page.download_plugin.click_first()
    page.wait_unit_redirect(old_link)
    page.download_web()
    file_size = page.get_exe_size_mb()
    page_download_size = page.fetch_download_size()
    with allure.step("Checking size"):
        assert file_size == page_download_size

@allure.story("Third test script")
def test_third_script():
    with allure.step("Main page"):
        main_page()
    with allure.step("Download page"):
        download_page()