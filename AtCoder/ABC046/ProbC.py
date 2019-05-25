from math import ceil
from fractions import Fraction
n = int(input())

nt, na = 1, 1
for i in range(n):
    rt, ra = list(map(int, input().split()))
    r = max([ceil(Fraction(nt, rt)), ceil(Fraction(na, ra))])
    nt = r*rt
    na = r*ra
    print(nt, na)

print(nt+na)
