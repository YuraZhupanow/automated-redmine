from pages.home_page import HomePage


class TestHomePage:
    def test_visit_home_page(self, driver):
        home_page = HomePage(driver)
        home_page.visit()
        assert home_page.FLASH_ERROR_TEXT_FIELD == "Redmine"
