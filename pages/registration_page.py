from selenium.webdriver.common.by import By
from .base_page import BasePage


class RegistrationPage(BasePage):
    LOGIN_INPUT = (By.ID, "user_login")
    PASSWORD_INPUT = (By.ID, "user_password")
    CONFIRMATION_INPUT = (By.ID, "user_password_confirmation")
    FIRST_NAME_INPUT = (By.ID, "user_firstname")
    LAST_NAME_INPUT = (By.ID, "user_lastname")
    EMAIL_INPUT = (By.ID, "user_mail")
    SUBMIT_BTN = (By.CSS_SELECTOR, "input[value='Submit']")

    def enter_login(self, user):
        self.find(self.LOGIN_INPUT).send_keys(user.username)

    def enter_password(self, user):
        password = user.password
        self.find(self.PASSWORD_INPUT).send_keys(password)
        self.find(self.CONFIRMATION_INPUT).send_keys(password)

    def enter_first_name(self, user):
        self.find(self.FIRST_NAME_INPUT).send_keys(user.first_name)

    def enter_last_name(self, user):
        self.find(self.LAST_NAME_INPUT).send_keys(user.last_name)

    def enter_email(self, user):
        self.find(self.EMAIL_INPUT).send_keys(user.email)

    def click_submit_btn(self):
        self.find(self.SUBMIT_BTN).click()
