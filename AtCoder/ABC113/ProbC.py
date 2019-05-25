n, m = map(int, input().split())
py = [list(map(int, input().split()))+[i+1] for i in range(m)]
py = sorted(py, key = lambda x: x[1])

ans = [0]*m
prefecs = [1]*(n+1)
for i, (p, y, j) in enumerate(py):
    top = p
    under = prefecs[p]
    ans[i] = (str(top).zfill(6)+str(under).zfill(6), j)
    prefecs[p] += 1

ans = sorted(ans, key = lambda x: x[1])
for i in range(m):
    print(ans[i][0])
