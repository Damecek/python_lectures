#!/usr/bin/env python3
""""""


def my_map(func, iter):
    return [func(it) for it in iter]


def rev(word):
    return word[::-1]


print(my_map(rev, ['asd', 'asdfgh', '1234567']))
