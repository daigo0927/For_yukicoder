n, m = map(int, input().split())
ab = [list(map(int, input().split())) for _ in range(m)]

inf = 10**9
lefts = [inf for _ in range(n+1)]
for a, b in ab:
    lefts[a] = min(lefts[a], b-1)

right = -1
ans = 0
for i in range(1, n+1):
    if lefts[i] == inf:
        continue
    if i > right:
        ans += 1
        right = lefts[i]
    else:
        right = min(lefts[i], right)
print(ans)
