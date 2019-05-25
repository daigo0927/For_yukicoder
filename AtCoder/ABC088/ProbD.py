from collections import deque
h, w = list(map(int, input().split()))
s = [input() for _ in range(h)]

dxs = [1, 0, -1, 0]
dys = [0, 1, 0, -1]

dists = [[3000]*w for _ in range(h)]
dists[0][0] = 1
que = deque([(0, 0, 1)])
while len(que) > 0:
    i, j, score = que.popleft()
    
    for dy, dx in zip(dys, dxs):
        i_next, j_next = i+dy, j+dx
        if i_next < 0 or i_next >= h or j_next < 0 or j_next >= w:
            continue
        if s[i_next][j_next] == '#':
            continue
        if dists[i_next][j_next] <= score+1:
            continue
        dists[i_next][j_next] = score+1
        que.append((i_next, j_next, score+1))
# for d in dists: print(d)

if dists[h-1][w-1] == 3000:
    print(-1)
    exit()
d_min = dists[h-1][w-1]
n_black = 0
for i in range(h):
    for j in range(w):
        if s[i][j] == '#':
            n_black += 1
print(h*w - n_black - d_min)
