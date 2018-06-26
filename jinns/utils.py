import random
import uuid


def make_token():
    return uuid.uuid4().hex


def make_random_slug(n=6, case='lower'):
    start = int('0xA%s' % ('0' * (n - 1)), 16)
    end = int('0x%s' % ('F' * n), 16)
    num = random.randint(start, end)
    code = hex(num)[2:]
    return code.lower() if case == 'lower' else code.upper()


