import heapq

n, m, s, t = map(int, input().split())
s, t = s-1, t-1
src = [tuple(map(int, input().split())) for i in range(m)]

es = [[] for i in range(n)]
for u, v, a, b in src:
    u, v = u-1, v-1
    es[u].append((v, a, b))
    es[v].append((u, a, b))

inf = float('inf')
cy = [inf]*n
cy[s] = 0
hq = [(0, s)]
heapq.heapify(hq)
while hq:
    cost, v = heapq.heappop(hq)
    for to, a, b in es[v]:
        if cost+a >= cy[to]:
            continue
        cy[to] = cost+a
        heapq.heappush(hq, (cy[to], to))

cs = [inf]*n
cs[t] = 0
hq = [(0, t)]
heapq.heapify(hq)
while hq:
    cost, v = heapq.heappop(hq)
    for to, a, b in es[v]:
        if cost+b >= cs[to]:
            continue
        cs[to] = cost+b
        heapq.heappush(hq, (cs[to], to))

ans = [inf]
for i in reversed(range(n)):
    tmp = cs[i]+cy[i]
    ans.append(min(ans[-1], tmp))

for a in reversed(ans[1:]):
    print(10**15-a)
    
