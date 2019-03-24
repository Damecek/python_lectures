#!/usr/bin/env python3
"""  dsfsd """

import random


def search(pos, what, ar):
    for i in range(len(ar)):
        if what == ar[i][pos]:
            return True


if __name__ == '__main__':
    with open('passwd') as f:
        p = [line.rstrip('\n').split(':') for line in f]
    new = [0, 0, 0, 0, 0, 0, 0]
    while True:
        new[0] = input('enter login name ')
        if not search(0, new[0], p):
            break
    while True:
        ri = random.randint(1, 1000)
        if not search(2, ri, p):
            break
    uid = input(f'suggest {ri} agree? y/n ')
    while True:
        new[2] = input('enter uid: ') if uid == 'n' else ri
        if not search(0, new[2], p):
            break
    home = input(f'i offer you this home: /home/{new[0]}, agree? y/n ')
    new[5] = input('enter home: ') if home == 'n' else 'home/' + new[0]

    bash = input('i offer you this bash: /bin/bash, agree? y/n ')
    new[6] = (input('enter bash: ') if bash == 'n' else 'bin/bash') + '\n'
    #TODO
    with open('passwd', 'a') as f:
        f.write(new)
    print(new)
