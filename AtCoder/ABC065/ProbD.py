import heapq

n = int(input())
xy = [list(map(int, input().split())) for _ in range(n)]
ixy = [(i, x, y) for i, (x, y) in enumerate(xy)]

# Get edges with cost along both x, y
edges = [[] for i in range(n)]
for x_or_y in [1, 2]:
    xy_sorted = sorted(ixy, key = lambda a: a[x_or_y])
    for i in range(n-1):
        i1 = xy_sorted[i][0]
        i2 = xy_sorted[i+1][0]
        cost = xy_sorted[i+1][x_or_y] - xy_sorted[i][x_or_y]
        edges[i1].append((i2, cost))
        edges[i2].append((i1, cost))

# Calculate minimum Spanning tree (Prim algorithm)
distinct = [False]*n
ans = 0
pque = []
heapq.heappush(pque, (0, 0))
while len(pque) > 0:
    # print(pque)
    cost, v = heapq.heappop(pque)
    if distinct[v]: continue
    
    ans += cost
    distinct[v] = True

    for v_next, cost_next in edges[v]:
        if not distinct[v_next]:
            heapq.heappush(pque, (cost_next, v_next))

print(ans)
