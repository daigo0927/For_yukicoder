n, m = list(map(int, input().split()))
dist_given = {}
dist = [[1000]*(n+1) for _ in range(n+1)]
for i in range(1, n+1): dist[i][i] = 0
for _ in range(m):
    a, b, c = list(map(int, input().split()))
    dist[a][b] = c
    dist[b][a] = c
    dist_given[tuple(sorted([a, b]))] = c

for k in range(1, n+1):
    for i in range(1, n+1):
        for j in range(1, n+1):
            dist[i][j] = min(dist[i][j], dist[i][k]+dist[k][j])
# print(dist)
ans = 0
for i in range(1, n):
    for j in range(i+1, n+1):
        if (i, j) in dist_given.keys() and dist[i][j] < dist_given[(i, j)]:
            ans += 1
print(ans)
