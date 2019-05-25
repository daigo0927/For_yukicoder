from collections import deque

n = int(input())
tree = {i:[] for i in range(1, n+1)}
for _ in range(n-1):
    u, v, w = map(int, input().split())
    tree[u].append((u, v, w))
    tree[v].append((v, u, w))

que = deque(tree[1])
dist = [-1]*(n+1)
dist[1] = 0
while len(que) > 0:
    u, v, w = que.popleft()
    dist[v] = dist[u]+w
    for un, vn, wn in tree[v]:
        if dist[vn] > 0:
            pass
        else:
            que.append((un, vn, wn))
            
for d in dist[1:]:
    print(0 if d%2 == 0 else 1)
