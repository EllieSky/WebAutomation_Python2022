def greeting(first_name, last_name=None, gender='F'):
    if last_name and gender.upper() == 'F':
        return f"How do you do Mrs. {last_name}?"
    elif last_name:
        return f"How do you do Mr. {last_name}?"
    else:
        return f"Hey {first_name}, I am happy to see you!"

# print("Hello Everyone!!!")
# age = 29
# name = '      Ellie Yampolskaya      '
#
# weight = 130.5
# print(age.bit_count())
# print(weight.is_integer())
#
# print(name.upper())
#
# name.split(' ')
# # message = 'Hello, my name is {name}, and I am {year} years old.'.format(name=name.strip(), year=age)
#
# message = f'Hello, my name is {name.strip()}, and I am {age} years old.'
# print(message)

# pass

# print(greeting("Jane"))
# print(greeting("John", "Doe", gender='M'))
# print(greeting("Anne", "Wintour"))
# print(greeting("Bobby", gender='M'))

sentence = "I am so glad it's almost Friday"
split_sent = sentence.split(' ')

# Create a function that takes a sentence and returns
# a sentence with the words in reverse order


def reverse_sentence(sentence):
    return ' '.join(sentence.split(' ')[::-1])
    #### OR same as code below
    # step1 = sentence.split(' ')
    # step2 = step1[::-1]
    # result = ' '.join(step2)
    # return result



print(reverse_sentence('I am here, where are you'))


# Bonus: Create a function is_palindrome. The function
# should take an input string, and return True if it
# is a palindrome, and False if it is not.
# Palindrome = same from front to back and back to front

