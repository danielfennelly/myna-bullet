import random
import string


def token(n=32):
    chars = random.sample(string.ascii_uppercase + string.digits, n)
    return ''.join(chars)
