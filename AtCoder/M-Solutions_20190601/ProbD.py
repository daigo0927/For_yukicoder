from collections import deque

n = int(input())
tree = {i:[] for i in range(1, n+1)}
for _ in range(n-1):
    a, b = map(int, input().split())
    tree[a].append(b)
    tree[b].append(a)
c = list(map(int, input().split()))

c = sorted(c, reverse = True)
d = [-1]*(n+1)
que = deque([1])
ic = 0
while len(que) > 0:
    x = que.popleft()
    d[x] = c[ic]
    ic += 1
    for y in tree[x]:
        if d[y] < 0:
            que.append(y)
print(sum(c[1:]))
print(*d[1:])
