from behave import step

from helpers.base_steps import BaseMethods


@step('')
def find_elem(context, ):

# Scenario: As an admin I should be able to login
# Given I open the http://http://hrm-online.portnov.com.url
#  When I enter text admin into the elements id=username
#  And I enter text password into the element id=txtPassword
# And I click the id=btnLogin element
#  Then the url should contain/pim/viewEmployeeList
#  And I get the text from element id=welcome
#  And the text should be Welcome Admin

@step('I find the elemt {by}={locator}')
def find_elem(context,by,locator):
    bm: BaseMethods = context.base_methods
    return bm.find_elem(by,locator)

@step ('I open the {url}url')
def open_url(context, url):
    context.browser.get(url)


@step ( 'I enter text {text} admin into the element {by}={locator}')
def enter_text(context,text,by,locator):
    find_elem(context,by,locator).send_keys(text)

    #OR
    context.base_methods.enter_text((by,locator),text)

    #
    # bm:BaseMethods = context.base_methods
    # bm.enter_text((by, locator),text)

@step('And I click the {by}={locator} element')
def click_element (context,by,locator):
    find_elem(context,by,locator).click()

@step('Then the url should contain{url}')
def url_contains(context,url):
 current_url=   context.browser.current_url
 assert  url in current_url

@step ('And I get the text from element {by}={locator}')
def get_text(context,by,locator):
    context.element_text=context.base_methods.get_text((by,locator))

@step(' the text should be {text}')
def is_text(context,text):
    assert text == context.element_text






