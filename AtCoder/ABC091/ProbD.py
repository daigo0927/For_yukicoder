# Greatly refered to the solution: https://atcoder.jp/contests/abc091/submissions/3549633
from sys import stdin
import numpy as np
ORD = 28

n = int(stdin.readline())
a = np.array(list(map(int, stdin.readline().split())))
b = np.array(list(map(int, stdin.readline().split())))

def search(a_, b_, pow2):
    c1 = np.searchsorted(a_, pow2 - b_)
    c2 = np.searchsorted(a_, 2*pow2 - b_)
    c3 = np.searchsorted(a_, 3*pow2 - b_)
    return n**2 - np.sum(c3) + np.sum(c2) - np.sum(c1)

a_ord = np.zeros((ORD, n), dtype = int)
b_ord = np.zeros((ORD, n), dtype = int)
for i in range(1, ORD+1):
    a_ord[i-1, :] = a%(2**i)
    b_ord[i-1, :] = b%(2**i)
a_ord = np.sort(a_ord, axis = 1)

ans = ''
for i in range(ORD):
    count = search(a_ord[i], b_ord[i], 2**i)
    ans += '0' if count%2 == 0 else '1'
    
count = search(a_ord[-1], b_ord[-1], 2**ORD)
ans += '0' if count%2 == 0 else '1'

print(int(ans[::-1], 2))
