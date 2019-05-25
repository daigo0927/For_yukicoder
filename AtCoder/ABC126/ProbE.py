from collections import deque

n, m = map(int, input().split())
xyz = {i:[] for i in range(1, n+1)}
for _ in range(m):
    x, y, z = map(int, input().split())
    xyz[x].append((x, y, z))
    xyz[y].append((y, x, z))
    
connects = [0]*(n+1)
group = 1
for i in range(1, n+1):
    if connects[i] > 0:
        continue
    if len(xyz[i]) == 0:
        connects[i] = group
        group += 1
        continue

    que = deque(xyz[i])
    connects[i] = group
    while len(que) > 0:
        x, y, z = que.popleft()
        connects[y] = group
        for xn, yn, zn in xyz[y]:
            if connects[yn] > 0:
                pass
            else:
                que.append((xn, yn, zn))
    group += 1
    
# print(connects)
print(max(connects))
