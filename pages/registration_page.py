from selenium.webdriver.common.by import By
from .base_page import BasePage
from faker import Faker


class RegistrationPage(BasePage):
    LOGIN_INPUT = (By.ID, "user_login")
    PASSWORD_INPUT = (By.ID, "user_password")
    CONFIRMATION_INPUT = (By.ID, "user_password_confirmation")
    FIRST_NAME_INPUT = (By.ID, "user_firstname")
    LAST_NAME_INPUT = (By.ID, "user_lastname")
    EMAIL_INPUT = (By.ID, "user_mail")
    SUBMIT_BTN = (By.CSS_SELECTOR, "input[value='Submit']")

    def enter_login(self):
        self.find(self.LOGIN_INPUT).send_keys(Faker().user_name())

    def enter_password(self):
        password = Faker().password()
        self.find(self.PASSWORD_INPUT).send_keys(password)
        self.find(self.CONFIRMATION_INPUT).send_keys(password)

    def enter_first_name(self):
        self.find(self.FIRST_NAME_INPUT).send_keys(Faker().first_name())

    def enter_last_name(self):
        self.find(self.LAST_NAME_INPUT).send_keys(Faker().last_name())

    def enter_email(self):
        self.find(self.EMAIL_INPUT).send_keys(Faker().email())

    def click_submit_btn(self):
        self.find(self.SUBMIT_BTN).click()
