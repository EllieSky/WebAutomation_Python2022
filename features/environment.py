import os
from behave import *
from selenium.webdriver.chrome import webdriver

from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager

from helpers.base_steps import BaseMethods
from tests import DEFAULT_WAIT, DOMAIN, PROJECT_PATH


# before_all/after_all
# before_feature/after_feature
# before_tag/after_tag
# before_step /after_feature

def before_scenario(context, scenario):
    if scenario.name == 'Count letters in a name':
        print('Not a SELENIUM scenario')
    context.url = DOMAIN
    context.browser = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    context.base_methods = BaseMethods(context.browser)
    context.wait = WebDriverWait(context.browser, DEFAULT_WAIT)
    context.browser.get(context.url)


def after_scenario(context, scenario):
    if context.satus.name == 'failed':
        output_folder_path = os.path.join(PROJECT_PATH, 'behaive_failed')

        if not os.path.exists(output_folder_path):
            os.mkdir(output_folder_path)

        scenario_name: str = scenario.name.replace('','_').lower()
        test_name_pieces = test_name.split('.')

        folder_path = output_folder_path
        for piece in test_name_pieces:
            folder_path = os.path.join(folder_path, piece)
            os.mkdir(folder_path)

            context.browser.save_screenshot(
                os.path.join(folder_path, 'screenshot.png')
            )


