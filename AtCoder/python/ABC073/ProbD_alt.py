from itertools import permutations
import heapq

INF = float('inf')
n, m, R = list(map(int, input().split()))
r = list(map(int, input().split()))

cost = {}
for i in range(m):
    a, b, c = list(map(int, input().split()))
    if not a in cost.keys():
        cost[a] = [(b, c)]
    else:
        cost[a].append((b, c))
    if not b in cost.keys():
        cost[b] = [(a, c)]
    else:
        cost[b].append((a, c))
        
dist = [[INF]*(n+1) for _ in range(n+1)]
for st in r:
    d = [INF]*(n+1)
    d[st] = 0
    path = [(0, st)]
    heapq.heapify(path)
    while len(path) > 0:
        c, node = heapq.heappop(path)
        if d[node] < c:
            continue
        d[node] = c
        for node_next, c_next in cost[node]:
            if d[node_next] < INF:
                continue
            heapq.heappush(path, (d[node]+c_next, node_next))
    dist[st] = d
# for d in dist: print(d)

ans = INF
for p in permutations(r):
    ans_ = 0
    for i in range(R-1):
        ans_ += dist[p[i]][p[i+1]]
    ans = min(ans, ans_)
print(ans)
