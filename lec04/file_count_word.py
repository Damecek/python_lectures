#!/usr/bin/env python3
"""prints number of individual words in file given as argument"""


import sys
from file_read_by_word import read_words

def read_individuals(file):
    """returns list of words from file"""
    words = read_words(file)
    individuals = [i for i in words if words.count(i) == 1]
    #individuals = [ind for ind in words if w_counter(ind).most_common() == 1]
    return individuals


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print(f'Bad usage: {__file__} <name of file>')
        exit()
    else:
        print(read_individuals(sys.argv[1]))
