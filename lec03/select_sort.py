#!/usr/bin/env python3
"""select sort"""


def select_sort(numb_list):
    """gets list a return sorted list using select sort"""
    for i in range(len(numb_list)):
        maxn = max(numb_list[i:])
        indexn = numb_list[i:].index(maxn) + i
        numb_list[indexn], numb_list[i] = numb_list[i], numb_list[indexn]
    return numb_list


if __name__ == "__main__":
    n_list = [3, 0, 342, 3 -5, -92, 342, 2424, 0, -1]
    print(select_sort(n_list))
