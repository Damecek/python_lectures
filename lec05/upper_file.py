#!/usr/bin/env python3
import sys


def upp_file(fname, param):
    w_list = []
    with open(fname) as f:
        if param == '-u':
            print(f.read().upper())
        elif param == '-l':
            print(f.read().lower())
        else:
            print('bad parametr')


if __name__ == '__main__':
    if len(sys.argv) != 3:
        print('bad usage upper_file.py <name of file> <-u upper -l lower>')
        exit()
    else:
        upp_file(sys.argv[1], sys.argv[2])
