from behave import step

from helpers.base_steps import BaseMethods


@step('I find the element {by}={locator}')
def find_elem(context, by, locator):
    bm: BaseMethods = context.base_methods
    return bm.find_elem((by, locator))

@step('I open the {url} url')
def open_url(context, url):
    context.browser.get(url)

@step('I enter text {text} into the element {by}={locator}')
def enter_text(context, text, by, locator):
    find_elem(context, by, locator).send_keys(text)
# OR
#     context.base_methods.enter_text((by, locator), text)

@step('I click the {by}={locator} element')
def click_element(context, by, locator):
    find_elem(context, by, locator).click()

@step('the url should contain {url}')
def url_contains(context, url):
    current_url: str = context.browser.current_url
    assert url in current_url

@step('I get the text from element {by}={locator}')
def get_text(context, by, locator):
    context.element_text = context.base_methods.get_text((by, locator))

@step('the text should be {text}')
def is_text(context, text):
    assert text == context.element_text
