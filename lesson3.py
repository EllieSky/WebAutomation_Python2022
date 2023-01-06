def isPalindrome(stri):
    stri = stri.lower()

    stri = ''.join(stri.split(' '))
    result = (stri == stri[::-1])
    return result


def ask_for_palindrome():
    stri = input('Please enter your input: ')
    if isPalindrome(stri):
        print("Yes, it is a palindrome")
    else:
        print("Nope, not a palindrome")


# ask_for_palindrome()
# print(isPalindrome("abcba"))  # True
# print(isPalindrome("cow"))  # False
# print(isPalindrome("Abcba"))   # True
# print(isPalindrome("Was it a car or a cat I saw")) # True


def num_to_power(num, pwr):
    if pwr == 0:
        return 1
    else:
        return num * num_to_power(num, pwr-1)


assert num_to_power(2, 3) == 8
assert num_to_power(3, 3) == 27


def recur_palindrome(strin):
    if len(str) == 1:
        return True
    else:
        return strin[0] == strin[-1] and recur_palindrome(strin[1:-1])


print(recur_palindrome("abcba"))  # True
print(recur_palindrome("cow"))  # False