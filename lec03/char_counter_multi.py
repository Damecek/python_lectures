#!/usr/bin/env python3
"""prints list of letters with frequency"""
import sys
from collections import Counter


def usage():
    print(f"bad usage: {__file__} <string>")


def letter_counter():
    let_counter = Counter
    file = open("bp.txt", "r")
    word_list = []
    for line in file:
        for word in line.split():
            for ch in word:
                word_list.append(ch.lower())
    return dict(let_counter(word_list[:]).most_common())


if __name__ == "__main__":
    if len(sys.argv) < 1:
        usage()
    else:
        tup = letter_counter()
        file_out = open("bp_char_count.txt", "w")
        j = 0
        for i in tup:
            j += 1
            print(f"{i}: {tup.get(i)} {'time' if tup.get(i) == 1 else 'times'} position: {j}.")
            file_out.writelines(f"{i} {tup.get(i)}\n")
