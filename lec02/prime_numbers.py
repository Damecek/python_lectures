#!/usr/bin/env python3
"""
prints primes between 2 arguments
"""
import sys


def usage():
    """
    prints usage of script
    """
    return "Usage prime_numbers.py <int from> <int to>\n\
script prints primes between 'from' and 'to'"


if __name__ == "__main__":
    if len(sys.argv) != 3:
        print(usage())
        exit()
    else:
        prime = True
        a = int(sys.argv[1])
        b = int(sys.argv[2])
        if a > b:
            c = a
            a = b
            b = c
        if a == 1:
            a = 2
        for i in range(a, b):
            for j in range(2, i):
                if i % j == 0:
                    prime = False
            if prime:
                print(i)
            prime = True