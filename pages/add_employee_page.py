from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

from pages.base_page import BasePage


class AddEmployeePage(BasePage):
    @property
    def PAGE_URL(self):
        return "/pim/addEmployee"

    @property
    def PAGE_NAME(self):
        return "Add Employee"

    def enter_employee_info(self, emp_id, first_name="Bob", last_name="Smith"):
        self.browser.find_element(By.ID, 'firstName').send_keys(first_name)
        self.browser.find_element(By.ID, 'lastName').send_keys(last_name)

        self.browser.find_element(By.ID, 'employeeId').clear()
        self.browser.find_element(By.ID, 'employeeId').send_keys(emp_id)

    def do_save(self):
        self.browser.find_element(By.ID, 'btnSave').click()

    def do_create_login_details(self, enable=True):
        check_box = self.browser.find_element(By.ID, 'chkLogin')
        if check_box.is_selected() is not enable:
            check_box.click()

    def enter_user_info(self, username, password="Bob", repassword=None):
        self.wait.until(EC.visibility_of_element_located(
            (By.ID, 'user_name'))).send_keys(username)
        self.wait.until(EC.visibility_of_element_located(
            (By.ID, 'user_password'))).send_keys(password)
        if not repassword:
            repassword = password
        self.wait.until(EC.visibility_of_element_located(
            (By.ID, 're_password'))).send_keys(repassword)