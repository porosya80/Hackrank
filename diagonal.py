#!/bin/python3

import sys


n = int(input().strip())
a = []
for a_i in range(n):
    a_t = [int(a_temp) for a_temp in input().strip().split(' ')]
    a.append(a_t)



diag = sum (([a[i][i] for i in range(n)]))              # [-2, -6, 7,  8]
bdiag =  sum (([a[n-1-i][i] for i in range(n-1,-1,-1)]))  # [ 2,  5, 2, -1]
print(abs(diag-bdiag))