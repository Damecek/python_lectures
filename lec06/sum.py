#!/usr/bin/env python3


def Sum(*args):
    val = 0
    for i in args:
        val += i
    return val


if __name__ == '__main__':
    print(Sum(1, 4, 2, 5, 2, 3, 4, 1, 123))
