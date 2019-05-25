from collections import deque
n, m = list(map(int, input().split()))
path = {}
ab = [list(map(int, input().split())) for i in range(m)]
for i in range(m):
    a, b = ab[i]
    if not a in path.keys():
        path[a] = [b]
    else:
        path[a].append(b)
    if not b in path.keys():
        path[b] = [a]
    else:
        path[b].append(a)

ans = 0
for i in range(m):
    a_tar, b_tar = ab[i]
    visit = [True] + [False]*n
    que = deque([1])
    while len(que) > 0:
        node = que.popleft()
        visit[node] = True
        for node_next in path[node]:
            if [node, node_next] == [a_tar, b_tar] or [node, node_next] == [b_tar, a_tar]:
                continue
            if visit[node_next]:
                continue
            que.append(node_next)
    if False in visit:
        ans += 1
print(ans)
