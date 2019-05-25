import sys
sys.setrecursionlimit(100000)

n, m = map(int, input().split())
ab = [list(map(int, input().split())) for _ in range(m)][::-1]

uf = [-1]*(n+1)
def find(i):
    if uf[i] < 0:
        return i
    else:
        uf[i] = find(uf[i])
        return uf[i]

ans = [n*(n-1)//2]
for i in range(m-1):
    a, b = ab[i]
    pa, pb = find(a), find(b)

    if pa != pb:
        pa, pb = (pb, pa) if uf[pb] < uf[pa] else (pa, pb) # swap (merge technique)
        ans.append(ans[i] - uf[pa]*uf[pb])
        uf[pa] += uf[pb]
        uf[pb] = pa
    else:
        ans.append(ans[i])
    # print(uf)

for ans_ in ans[::-1]:
    print(ans_)
