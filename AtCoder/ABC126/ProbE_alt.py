from collections import deque

n, m = map(int, input().split())
xyz = []
for _ in range(m):
    x, y, z = map(int, input().split())
    xyz.append((x, y, z))


uf = [-1]*(n+1)
def find(i):
    if uf[i] < 0:
        return i
    else:
        uf[i] = find(uf[i])
        return uf[i]

for x, y, z in xyz:
    px, py = find(x), find(y)
    
    if px != py:
        px, py = (px, py) if uf[py] < uf[px] else (px, py)
        uf[px] += uf[py]
        uf[py] = px

# print(uf)
ans = sum([1 for i in range(1, n+1) if uf[i] < 0])
print(ans)
