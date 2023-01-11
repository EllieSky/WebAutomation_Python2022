from abc import abstractmethod

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from helpers.base_steps import BaseMethods
from tests import BASE_URL


class BasePage(BaseMethods):
    def __init__(self, browser: webdriver.Remote):
        super().__init__(browser)
        self.browser = browser
        self.wait = WebDriverWait(self.browser, 5)

    def get_header(self):
        return self.wait.until(expected_conditions.presence_of_element_located(
                (By.CSS_SELECTOR, '.box .head h1'))).text
                # (By.CSS_SELECTOR, '.personalDetails .head h1'))).text

    def go_to_page(self):
        self.browser.get(BASE_URL + self.PAGE_URL)
        self.browser.get(f'{BASE_URL}{self.PAGE_URL}')

    @property
    @abstractmethod
    def PAGE_NAME(self):
        pass

    @property
    @abstractmethod
    def PAGE_URL(self):
        pass
