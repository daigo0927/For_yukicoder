from collections import deque
INF = 10**6
n = int(input())
path = {}
for i in range(n-1):
    a, b = list(map(int, input().split()))
    if not a in path.keys():
        path[a] = [b]
    else:
        path[a].append(b)
    if not b in path.keys():
        path[b] = [a]
    else:
        path[b].append(a)
# print(path)

dist_f = [INF]*(n+1)
dist_f[1] = 0
que_f = deque([1])
while len(que_f) > 0:
    st_f = que_f.popleft()
    for en_f in path[st_f]:
        if dist_f[en_f] == INF:
            dist_f[en_f] = dist_f[st_f]+1
            que_f.append(en_f)

dist_s = [INF]*(n+1)
dist_s[n] = 0
que_s = deque([n])
while len(que_s) > 0:
    st_s = que_s.popleft()
    for en_s in path[st_s]:
        if dist_s[en_s] == INF:
            dist_s[en_s] = dist_s[st_s]+1
            que_s.append(en_s)
# print(dist_f, dist_s)

count_f, count_s = 0, 0
for d_f, d_s in zip(dist_f[1:], dist_s[1:]):
    if d_f <= d_s:
        count_f += 1
    else:
        count_s += 1
if count_f > count_s:
    print('Fennec')
else:
    print('Snuke')
