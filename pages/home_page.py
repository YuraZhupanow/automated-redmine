from selenium.webdriver.common.by import By
from .base_page import BasePage


class HomePage(BasePage):
    REGISTER_BTN = (By.CLASS_NAME, "register")
    FLASH_ERROR_TEXT_FIELD = (By.ID, "flash_error")

    def visit(self):
        self.driver.get("http://localhost:3000/")

    def click_register_btn(self):
        self.find(self.REGISTER_BTN).click()

    def verify_user_is_registered(self):
        confirmation_text = "Your account was created and is now pending administrator approval."
        assert self.find(self.FLASH_ERROR_TEXT_FIELD).text == confirmation_text
