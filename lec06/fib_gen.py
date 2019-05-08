#!/usr/bin/env python3
"""fibonacci numb generator"""


def fib(n):
    if n <= 1:
        return 1
    else:
        return fib(n - 1) + fib(n - 2)


def fib_gen(n):
    for i in range(n):
        yield fib(i)


for i in fib_gen(10):
    print(i)
