# encoding: utf-8

"""
taken from reddit's source code
"""

def to_base(q, alphabet):
    if q < 0:
        raise ValueError, "Must supply a positive integer"
    l = len(alphabet)
    converted = []
    while q != 0:
        q, r = divmod(q, l)
        converted.insert(0, alphabet[r])
    return "".join(converted) or alphabet[0]

def to36(q):
    return to_base(q, '0123456789abcdefghijklmnopqrstuvwxyz')

