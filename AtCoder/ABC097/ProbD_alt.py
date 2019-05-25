from collections import deque
n, m = map(int, input().split())
p = list(map(int, input().split()))
par = list(range(n+1))

def find(x):
    p_ = par[x]
    if p_ == x:
        return x
    a = find(p_)
    par[x] = a
    return a

for _ in range(m):
    x, y = map(int, input().split())
    bx, by = find(x), find(y)
    par[y] = bx
    par[by] = bx

ans = 0
for i in range(1, n+1):
    if find(i) == find(p[i-1]):
        ans += 1
print(ans)
