from behave import given, when, then, step


@step('my string is {name}')
@given('my name is {name}')
def input_name(context, name):
    context.my_name = name

@when('I count the letters in a string')
@step('I calculate the length of my name')
@when('I count the letters in my name')
def count_letters(context):
    context.my_name_count = len(context.my_name)


@then('There are {count} letters in total')
def expect_letter_count(context, count):
    assert int(count) == context.my_name_count,\
        f'Expected count to be {count} but it was actually {context.my_name_count}'
