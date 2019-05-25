from itertools import permutations

INF = float('inf')
n, m, R = list(map(int, input().split()))
r = list(map(int, input().split()))
dist = [[INF]*(n+1) for _ in range(n+1)]
for i in range(1, n+1):
    dist[i][i] = 0
for i in range(m):
    a, b, c = map(int, input().split())
    dist[a][b] = c
    dist[b][a] = c

from scipy.sparse import csgraph
dist = csgraph.floyd_warshall(dist)
# for k in range(n):
#     for i in range(n):
#         for j in range(n):
#             dist[i][j] = min(dist[i][j], dist[i][k]+dist[k][j])
# for d in dist: print(d)

ans = INF
for p in permutations(r):
    ans_ = 0
    for i in range(R-1):
        ans_ += dist[p[i]][p[i+1]]
    ans = min(ans, ans_)
print(int(ans))
