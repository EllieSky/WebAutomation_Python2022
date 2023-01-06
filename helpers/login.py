from selenium.webdriver.common.by import By


def login(browser, username='admin', password='password'):
    browser.find_element(By.ID, 'txtUsername').send_keys(username)
    browser.find_element(By.ID, 'txtPassword').send_keys(password)
    browser.find_element(By.ID, 'btnLogin').click()