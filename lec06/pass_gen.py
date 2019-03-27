#!/usr/bin/env python3
"""presents function that generates pass given length """


def gen(leng, spec=0):
    CH = string.digits + string.ascii_lowercase + string.ascii_uppercase
    SP = string.punctuation
    temp = ''.join(random.sample(SP, spec)) + ''.join(random.sample(CH, leng - spec))
    return ''.join(random.sample(temp, leng))


if __name__ == '__main__':
    import random
    import sys
    import string
    if len(sys.argv) == 3:
        print(gen(int(sys.argv[1]), int(sys.argv[2])))
    elif len(sys.argv) == 2:
        print(gen(int(sys.argv[1])))
    else:
        print('Bad usage')
