import re
print('kind input password')
password = input()


def passChecker(password):
    if len(password) < 6 or len(password) > 12:
        print('The password should have at least 6 characters but not more than 12.')
    elif not re.search("[a-z]", password):
        print('The password should have at least one lower case character')
    elif not re.search("[A-Z]", password):
        print('The password should have at least one uppercase character')
    elif not re.search("[0-9]", password):
        print('The password should have at least one numerical character')
    elif not re.search("[_@$]", password):
        print('The password should contain at least one special character ($, _, or @)')
    else:
        print("The password is Valid")
    return passChecker


passChecker(password)
