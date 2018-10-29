from collections import deque
n, m = map(int, input().split())
p = list(map(int, input().split()))
paths = {}
for _ in range(m):
    x, y = map(int, input().split())
    if not x in paths.keys():
        paths[x] = [y]
    else:
        paths[x].append(y)
    if not y in paths.keys():
        paths[y] = [x]
    else:
        paths[y].append(x)

connected = [None]*(n+1)
path_id = 1
for i in range(1, n+1):
    if connected[i] is None:
        connected[i] = path_id
    else:
        continue

    if i in paths.keys():
        stack = deque(paths[i])
        cluster = set([i]+paths[i])
    else:
        stack = []
    while len(stack) > 0:
        j = stack.pop()
        connected[j] = path_id
        for k in paths[j]:
            if connected[k] is None and not k in cluster:
                stack.append(k)
                cluster.add(k)
    path_id += 1
# print(connected)

ans = 0
for i in range(n):
    if connected[i+1] == connected[p[i]]:
        ans += 1
print(ans)
