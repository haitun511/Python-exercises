import re


def check(password):
    if len(password) >= 10 and \
            re.search("\d", password) and \
            re.search("[A-Z]", password) and \
            re.search("[a-z]", password):

        return True

    else:
        return False

