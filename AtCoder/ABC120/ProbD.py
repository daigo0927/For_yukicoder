import sys
sys.setrecursionlimit(100000)

n, m = map(int, input().split())
ab = [list(map(int, input().split())) for _ in range(m)][::-1]

par, sizes = [-1]*(n+1), [1]*(n+1)
def find(i):
    if par[i] < 0:
        return i
    else:
        par[i] = find(par[i])
        return par[i]

ans = [n*(n-1)//2]
for i in range(m-1):
    a, b = ab[i]
    pa, pb = find(a), find(b)

    if pa != pb:
        ans.append(ans[i] - sizes[pa]*sizes[pb])
        par[pa] = pb
        sizes[pb] += sizes[pa]
    else:
        ans.append(ans[i])
    # print(par, sizes)

for ans_ in ans[::-1]:
    print(ans_)
