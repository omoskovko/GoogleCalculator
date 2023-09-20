import string
from random import choice


def gen_pwd(pwd_len=10):
    len1 = pwd_len // 3
    len2 = pwd_len - len1 * 2
    s1 = "".join([choice(string.ascii_uppercase) for v in range(len1)])
    s2 = "".join([choice(string.digits) for v in range(len1)])
    s3 = "".join([choice(string.ascii_lowercase) for v in range(len2)])
    return s1 + s2 + s3


print(gen_pwd())
