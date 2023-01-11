import unittest

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager

from menus.main_menu import MainMenu
from menus.welcome_menu import WelcomeMenu
from pages.add_employee_page import AddEmployeePage
from pages.employee_information_page import EmployeeInformationPage
from pages.login_page import LoginPage
from pages.personal_details_page import PersonalDetailsPage
from pages.system_users_page import SystemUsersPage
from tests import DEFAULT_WAIT, DOMAIN


class SetupTest(unittest.TestCase):
    def setUp(self) -> None:
        self.url = DOMAIN
        self.browser = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        self.browser.get(self.url)
        self.wait = WebDriverWait(self.browser, DEFAULT_WAIT)
        self.login_page = LoginPage(self.browser)
        self.emp_info = EmployeeInformationPage(self.browser)
        self.add_emp = AddEmployeePage(self.browser)
        self.personal_details = PersonalDetailsPage(self.browser)
        self.main_menu = MainMenu(self.browser)
        self.welcome_menu = WelcomeMenu(self.browser)
        self.sys_user = SystemUsersPage(self.browser)

    def tearDown(self) -> None:
        self.browser.quit()


class AdminAuthTest(SetupTest):
    def setUp(self) -> None:
        super().setUp()
        self.login_page.login()


class TearDown(unittest.TestCase):
    def tearDown(self) -> None:
        print('Done')
