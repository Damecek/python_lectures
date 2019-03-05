#!/usr/bin/env python3
"""prints list of letters with frequency"""
import sys
from collections import Counter


def usage():
    print(f"bad usage: {__file__} <string>")


def letter_counter():
    let_counter = Counter
    return dict(let_counter(sys.argv[1]).most_common())


if __name__ == "__main__":
    if len(sys.argv) != 2:
        usage()
    else:
        tup = letter_counter()
        for i in tup:
            print(f"{i}: {tup.get(i)} {'time' if tup.get(i) == 1 else 'times'}")
