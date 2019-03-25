#!/usr/bin/env python3
"""like linux cut tool"""

from sys import argv as arg


def columns(param, l):
    if param[0] == '-':
        return range(int(param.strip('-')))
    if param[-1] == '-':
        return range(int(param.strip('-')) - 1, l)
    if param.isdigit():
        return range(int(param) - 1, int(param))
    if (param[0].isdigit()) & (param[-1].isdigit()):
        return range(int(param.split('-')[0]) - 1, int(param.split('-')[1]))
    return []


if len(arg) != 5:
    print('Bad usage: cut.py -d "char" -f "which column"')
    exit()
else:
    test_str = 'sdf.dsfasdf.as:asdf:Adf.sdfaSD:fsdf.sdfsD:Fsdfs.,s-.sa.fSAF:sdf.A:df.as.fdsdf'
    if arg[1] == '-d':
        delim, col_par = arg[2], arg[4]
    else:
        delim, col_par = arg[4], arg[2]
    del_str = test_str.split(delim)
    cols = columns(col_par, len(del_str))
    [print(test_str.split(delim)[i]) for i in cols]
