#!/usr/bin/env python3
"""
creates list of tuples
"""

tup = []
if __name__ == "__main__":
    for i in range(1, 11):
        for j in range(1, 11):
            tup.append((i, j, i*j))
    print(tup)
