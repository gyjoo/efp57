# The output of this code is modified to practice Exceptions
# This authentication system follows Apple Password Policy
# Reference : https://docs.python.org/release/2.5.2/lib/string-methods.html

class PasswordException(Exception):
    def __init__(self, value):
        self.parameter = value
    def __str__(self):
        return repr(self.parameter)

try:
    password = input("Enter new password ")

    if len(password) <= 8:
        raise PasswordException("Must be longer than 8 characters")
    elif password.islower() or password.isupper():
        raise PasswordException("Must include at least one Upper & Lowercase letter")
    elif password.isalnum() and password.isalpha():
        raise PasswordException("Must be a combination of numbers and characters")
    elif password.isspace():
        raise PasswordException("Must not include any white spaces")
    else:
        print("Congratulations! Your password is set into %s" % password)

except PasswordException as msg:
    print (msg)