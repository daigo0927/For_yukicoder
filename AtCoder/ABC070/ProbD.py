from collections import deque

n = int(input())
path = {}
for i in range(n-1):
    a, b, c = list(map(int, input().split()))
    if not a in path.keys():
        path[a] = [(b, c)]
    else:
        path[a].append((b, c))
        
    if not b in path.keys():
        path[b] = [(a, c)]
    else:
        path[b].append((a, c))
q, k = list(map(int, input().split()))
xy = [list(map(int, input().split())) for _ in range(q)]

dist = [None]*(n+1)
dist[k] = 0
que = deque([(k, 0)])
while len(que) > 0:
    node, d = que.popleft()
    dist[node] = d
    for node_next, d_next in path[node]:
        if dist[node_next] is None:
            que.append((node_next, d+d_next))
# print(dist)

for x, y in xy:
    print(dist[x]+dist[y])
