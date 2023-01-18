import time
import unittest
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager


class MyTestCase(unittest.TestCase):
    def __init__(self, methodName='runTest'):
        super().__init__(methodName)

    def setUp(self):
        self.url = "http://hrm-online.portnov.com/"
        self.browser = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        self.browser.get(self.url)
        time.sleep(3)

    def test_login_page_loads(self):
        browser = self.browser
        # browser = webdriver.Chrome(service=Service('/Users/ellie/Portnov2022/TestAutomation/drivers/chromedriver'))
        # browser.get("http://hrm.portnov.com/")
        self.assertEqual('OrangeHRM', browser.title)  # add assertion here
        btn_value = browser.find_element(By.ID, 'btnLogin').get_attribute('value')
        self.assertEqual('LOGIN', btn_value)
        panel_header = browser.find_element(By.ID, 'logInPanelHeading').text
        self.assertEqual('LOGIN Panel', panel_header)
        self.assertIn('/auth/login', browser.current_url)

    def test_valid_login(self):
        browser = self.browser
        username = 'admin'
        password = 'password'

        browser.find_element(By.ID, 'txtUsername').send_keys(username)
        browser.find_element(By.ID, 'txtPassword').send_keys(password)
        browser.find_element(By.ID, 'btnLogin').click()
        time.sleep(3)
        self.assertIn('/pim/viewEmployeeList', browser.current_url)
        message = browser.find_element(By.ID, 'welcome').text
        self.assertEqual("Welcome Admin", message)

        welcome_elem = browser.find_element(By.ID, 'welcome')

        browser.execute_script('arguments[0].click()', welcome_elem)
        self.assertTrue(browser.find_element(By.ID, 'welcome-menu').is_displayed())

        action = ActionChains(browser)
        action.move_to_element(browser.find_element(By.LINK_TEXT, 'Logout'))
        action.click()
        action.perform()













if __name__ == '__main__':
    unittest.main()
