import re

def set_name(firstName, middleName, lastName):
    '''This function is incomplete since it didn't implement middleName rules'''

    if len(firstName) < 3 or len(firstName) > 30:
        return False

    if len(lastName) < 3 or len(lastName) > 50:
        return False

    if not bool(re.match("^[A-Za-z-]*$", f"{firstName}")):
        return False

    if not bool(re.match("^[A-Za-z- ]*$", f"{lastName}")):
        return False


    return True
