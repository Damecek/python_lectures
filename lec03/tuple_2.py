#!/usr/bin/env python3
"""
creates list of tuples
"""

odd = []
even = []
if __name__ == "__main__":
    for i in range(1, 11):
        for j in range(1, 11):
            if i % 2 == 0:
                even.append((i, j, i*j))
            else:
                odd.append((i,j,i*j))
    print(odd)
    print(even)
