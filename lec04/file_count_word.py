#!/usr/bin/env python3
"""prints number of individual words in file given as argument"""


import sys
from collections import Counter

def read_individuals(file):
    """returns list of words from file"""
    try:
        with open(file) as f:
            w_counter = Counter
            words = f.read().split()
            individuals = [ind for ind in words if w_counter(words).most_common() == 1]
    except FileNotFoundError:
        print("file wasn't found!")
        exit()
    return individuals


if __name__ == "__main__":
    sys.argv.append("test.txt")
    if len(sys.argv) != 2:
        print(f'Bad usage: {__file__} <name of file>')
        exit()
    else:
        print(read_individuals(sys.argv[1]))
