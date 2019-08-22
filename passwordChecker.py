#! /usr/bin/python3
"""
program to check the validity or a password using given conditions i.e.
At least 1 letter between [a-z]
At least 1 number between [0-9]
At least 1 letter between [A-Z]
At least 1 character from [$#@]
Minimum length of transaction password: 6
Maximum length of transaction password: 12
"""
import re

print("Enter your password below: ")
password = input()
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
