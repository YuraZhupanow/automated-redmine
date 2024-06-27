from pages.home_page import HomePage
from pages.registration_page import RegistrationPage
from data.user_data import User


class TestRegistration:
    def test_registration(self, driver):
        new_user = User.create()
        home_page = HomePage(driver)
        home_page.visit()
        home_page.click_register_btn()
        registration_page = RegistrationPage(driver)
        registration_page.enter_login(new_user)
        registration_page.enter_password(new_user)
        registration_page.enter_first_name(new_user)
        registration_page.enter_last_name(new_user)
        registration_page.enter_email(new_user)
        registration_page.click_submit_btn()
        home_page.verify_user_is_registered()

