from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions

from pages.base_page import BasePage
from tests import ADMIN_USERNAME, ADMIN_PASSWORD


class LoginPage(BasePage):

    @property
    def PAGE_URL(self):
        return "/auth/login"

    @property
    def PAGE_NAME(self):
        return "LOGIN Panel"

    def get_header(self):
        return self.wait.until(expected_conditions.presence_of_element_located(
            (By.ID, 'logInPanelHeading'))).text

    def login(self, username=ADMIN_USERNAME, password=ADMIN_PASSWORD):
        browser = self.browser
        browser.find_element(By.ID, 'txtUsername').send_keys(username)
        browser.find_element(By.ID, 'txtPassword').send_keys(password)
        browser.find_element(By.ID, 'btnLogin').click()

    # forgotPassword
    # getCopyright

