import os

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager
from behave import *

from helpers.base_steps import BaseMethods
from tests import DOMAIN, DEFAULT_WAIT, PROJECT_PATH


# before_all / after_all
# before_feature / after_feature
# before_tag / after_tag
# before_step / after_step

def before_scenario(context, scenario):
    if "no_selenium" in scenario.effective_tags:
        return
    context.url = DOMAIN
    context.browser = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    context.base_methods = BaseMethods(context.browser)
    context.wait = WebDriverWait(context.browser, DEFAULT_WAIT)
    context.browser.get(context.url)


def after_scenario(context, scenario):
    if "no_selenium" in scenario.effective_tags:
        return
    if context.failed:
        output_folder_path = os.path.join(PROJECT_PATH, 'behave_failed_tests')

        if not os.path.exists(output_folder_path):
            os.mkdir(output_folder_path)

        scenario_name: str = scenario.name.replace(' ', '_').lower()

        folder_path = os.path.join(output_folder_path, scenario_name)
        if not os.path.exists(folder_path):
            os.mkdir(folder_path)

        context.browser.save_screenshot(
            os.path.join(folder_path, 'screenshot.png')
        )

        page_source = context.browser.page_source
        file = open(os.path.join(folder_path, 'source.html'), 'w')
        file.write(page_source)
        file.close()

    context.browser.quit()
