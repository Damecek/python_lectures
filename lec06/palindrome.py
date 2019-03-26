#!/usr/bin/env python3


def palindrome(wrd):
    return wrd.replace(' ', '') == wrd.replace(' ', '')[::-1]


if __name__ == '__main__':
    import sys
    print(palindrome(sys.argv[1]))
