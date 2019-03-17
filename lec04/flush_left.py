#!/usr/bin/env python3
"""flush left text in file with given length"""


def read_words(file):
    """returns list of words from file"""
    try:
        with open("test.txt", "r") as f:
            return f.read().split()
    except FileNotFoundError:
        print("file wasn't found!")


def write_words(file, l, words, oFile):
    """writes file with given length on line"""
    with open(oFile, "w") as f:
        line = words[0]
        for word in words[1:]:
            if len(line) + len(word) + 1 > l:
                f.write(line + "\n")
                line = word
            else:
                line += " " + word
        f.write(line)


if __name__ == "__main__":
    import sys
    if len(sys.argv) not in [3, 4]:
        print(f"Bad usage: {__file__} <name of file> <numb of char>")
        exit()
    else:
        write_words(sys.argv[1], int(sys.argv[2]), read_words(sys.argv[1]), sys.argv[1] if sys.argv[-1].isdigit == False else sys.argv[-1])
