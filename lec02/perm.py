#!/usr/bin/env python3
"""
take string arg and prints all perm
"""
import sys


def perm(in_list):
    """
    gets string for every char extracts and put at start and perm the rest
    :return permed strings:
    """
    if len(in_list) == 0:
        return []
    if len(in_list) == 1:
        return [in_list]
    out_list = []
    for i in range(len(in_list)):
        m = in_list[i]
        rem_list = in_list[:i] + in_list[i + 1:]
        # p = []
        for p in perm(rem_list):
            out_list.append([m] + p)
    return out_list


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage perm.py <string> returns all permutations of string")
    else:
        for p in perm(list(sys.argv[1])):
            for j in range(len(p)):
                print(p[j], end='')
            print('')