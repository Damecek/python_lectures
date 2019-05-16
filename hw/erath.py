#!/usr/bin/env python3
"""Sieve of Eratosthenes"""
import sys


def sieve(n):
    ps = [True for i in range(n + 1)]
    p = 2
    while p**2 < n - 1:
        if ps[p]:
            for i in range(p * 2, n + 1, p):
                ps[i] = False
        p += 1
    return [i for i in range(2, n + 1) if ps[i]]


sys.stdout.write(str(len(sieve(int(sys.stdin.read())))))
