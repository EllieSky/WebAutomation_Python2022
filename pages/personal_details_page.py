from selenium.webdriver.common.by import By

from pages.base_page import BasePage


class PersonalDetailsPage(BasePage):

    @property
    def PAGE_URL(self):
        return "/pim/viewEmployee/empNumber/3250"

    @property
    def PAGE_NAME(self):
        return 'Personal Details'

    def get_first_name(self):
        return self.browser.find_element(By.ID, 'personal_txtEmpFirstName').get_attribute('value')

    def get_last_name(self):
        return self.browser.find_element(By.ID, 'personal_txtEmpLastName').get_attribute('value')

    def get_employee_id(self):
        return self.browser.find_element(By.ID, 'personal_txtEmployeeId').get_attribute('value')

    def get_all_personal_info(self):
        return {
            'first_name': self.get_first_name(),
            'last_name': self.get_last_name(),
            'employee_id': self.get_employee_id(),
        }



