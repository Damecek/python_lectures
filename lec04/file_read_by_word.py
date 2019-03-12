#!/usr/bin/env python3
"""prints list of word from file given as argument"""

import sys


def read_words(file):
    """returns list of words from file"""
    try:
        with open(file) as f:
            return f.read().split()
    except FileNotFoundError:
        print("file wasn't found!")


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print(f'Bad usage: {__file__} <name of file>')
        exit()
    else:
        print(read_words(sys.argv[1]))
