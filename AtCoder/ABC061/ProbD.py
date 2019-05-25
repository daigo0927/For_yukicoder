INF = float('inf')
n, m = list(map(int, input().split()))
a, b, c = [], [], []
for _ in range(m):
    abc = list(map(int, input().split()))
    a.append(abc[0])
    b.append(abc[1])
    c.append(-abc[2]) # convert pos-neg

dist = [INF]*(n+1)
dist[1] = 0
for loop in range(n-1):
    for i in range(m):
        if dist[a[i]] == INF:
            continue
        if dist[b[i]] > dist[a[i]] + c[i]:
            dist[b[i]] = dist[a[i]] + c[i]
ans = dist[-1]

negative = [False]*(n+1) # negative closed path
for loop in range(n):
    for i in range(m):
        if dist[a[i]] == INF:
            continue
        if dist[b[i]] > dist[a[i]] + c[i]:
            dist[b[i]] = dist[a[i]] + c[i]
            negative[b[i]] = True
        if negative[a[i]] is True:
            negative[b[i]] = True

    if negative[-1] is True:
        break
# print(dist, negative)
if negative[-1] is True:
    print('inf')
else:
    print(-ans)
