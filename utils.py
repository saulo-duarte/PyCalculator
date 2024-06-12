import re

NUM_OR_DOT_REGEX = re.compile(r'^[0-9.]+$')

def is_number_or_dot(s):
    return bool(NUM_OR_DOT_REGEX.match(s))

def is_empty(s):
    return len(s) == 0

def isValidNumber(s):
    try:
        float(s)
        return True
    except ValueError:
        return False