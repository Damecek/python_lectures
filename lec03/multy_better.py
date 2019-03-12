#!/usr/bin/env python3
odd = [(i,j,i*j) for i in range(1,11) for j in range(1,11) if i % 2 == 0]
print(odd)
