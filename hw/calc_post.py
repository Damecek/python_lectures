#!/usr/bin/env python3
"""calculator, postfix"""
import sys


def operation(b, a, operator):
    if operator == '+':
        return a + b
    if operator == '-':
        return a - b
    if operator == '*':
        return a * b
    if operator == '/' and b != 0:
        return int(a / b)
    return ''


if __name__ == "__main__":
    for argv in sys.stdin:
        stack = []
        #print(argv.strip().split(' '))
        if argv.strip().split(' ')[0] != '':
            for i in argv.strip().split(' '):
                # print('-' + i)
                if i.isdigit():
                    stack.append(int(i))
                elif len(stack) > 1:
                    stack.append(operation(stack.pop(), stack.pop(), i))
                    if stack[len(stack) - 1] == '':
                        print("Zero division")
                        stack = []
                        break
                else:
                    print("Malformed expression")
                    stack = []
                    break
            if len(stack) == 1:
                print(stack.pop())
            #else:
            #    print("Malformed expression")