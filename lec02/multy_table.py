#!/usr/bin/env python3
"""takes argument and prints multy-table"""

import sys

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Bad usage -> {} int".format(__file__))
        exit(6)
    for i in range(1, 11):
        print(f"{i:>{len(sys.argv[1]) + 1}} * {sys.argv[1]:>{len(sys.argv[1])}} = {i * int(sys.argv[1]):>{len(sys.argv[1]) + 1}}")
