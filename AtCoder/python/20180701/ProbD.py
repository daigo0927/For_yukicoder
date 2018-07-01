from itertools import accumulate
from bisect import bisect_left, bisect_right

n = int(input())
a = list(map(int, input().split()))

ts = list(accumulate(a))+[0]
r = 0

def calc(st, ed):
    t0 = ts[ed-1] - ts[st-1]
    i1 = bisect_left(ts, (ts[ed-1]+ts[st-1])/2, st+1, ed-1)
    t11 = ts[i1-1] - ts[st-1]
    t12 = t0 - t11
    t21 = ts[i1] - ts[st-1]
    t22 = t0 - t21
    if abs(t22-t21) > abs(t12-t11):
        return t11, t12
    else:
        return t21, t22

ans = 10**18
for i in range(2, n-1):
    r1, r2 = calc(0, i)
    r3, r4 = calc(i, n)
    # print(r1, r2, r3, r4)
    diff = max([r1, r2, r3, r4]) - min([r1, r2, r3, r4])
    ans = min(ans, diff)

print(ans)
    

