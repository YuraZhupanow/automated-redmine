from pages.home_page import HomePage
from pages.registration_page import RegistrationPage


class TestRegistration:
    def test_registration(self, driver):
        home_page = HomePage(driver)
        home_page.visit()
        home_page.click_register_btn()
        registration_page = RegistrationPage(driver)
        registration_page.enter_login()
        registration_page.enter_password()
        registration_page.enter_first_name()
        registration_page.enter_last_name()
        registration_page.enter_email()
        registration_page.click_submit_btn()
        home_page.verify_user_is_registered()

