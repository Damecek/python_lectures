#!/usr/bin/env python3
"""calculator, postfix"""
import sys


def usage():
    """prints usage info & exits script"""
    print(f"Bad usage: {__file__} <string: numbers and operators in postfix notation>")
    exit()


def operation(b, a, operator):
    if operator == '+':
        return a + b
    if operator == '-':
        return a - b
    if operator == '*':
        return a * b
    if operator == '/' and b != 0:
        return a/b
    return ''


if __name__ == "__main__":
    if len(sys.argv) < 2:
        usage()
    else:
        stack = []
        for i in sys.argv[1:]:
            if i.isdigit():
                stack.append(int(i))
            elif len(stack) > 1:
                stack.append(operation(stack.pop(), stack.pop(), i))
                if stack[len(stack) - 1] == '':
                    print("Zero division")
                    exit(0)
            else:
                print("Malformed expression")
                exit()
        print(stack.pop())
