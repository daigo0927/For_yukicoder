import numpy as np
from collections import deque
h, w = map(int, input().split())
s = [input() for _ in range(h)]

segment = [[0]*w for _ in range(h)]
idx = 1
dxy = [[1, 0], [0, 1], [-1, 0], [0, -1]]
for y in range(h):
    for x in range(w):
        if segment[y][x] == 0:
            segment[y][x] = idx
            state = s[y][x]
            que = deque([[y, x, state]])
            while len(que) > 0:
                y_cur, x_cur, state = que.popleft()
                for dx, dy in dxy:
                    y_next = y_cur + dy
                    x_next = x_cur + dx
                    state_next = '.' if state == '#' else '#'
                    if x_next < 0 or y_next < 0 or x_next >= w or y_next >= h:
                        continue
                    elif s[y_next][x_next] != state_next:
                        continue
                    elif segment[y_next][x_next] == 0:
                        segment[y_next][x_next] = idx
                        que.append((y_next, x_next, state_next))
            idx += 1

# print(segment)
idx_max = idx
nbw = [[0, 0] for _ in range(idx_max+1)]
for y in range(h):
    for x in range(w):
        idx = segment[y][x]
        if s[y][x] == '#':
            nbw[idx][0] += 1
        else:
            nbw[idx][1] += 1
ans = 0
for nb, nw in nbw:
    ans += nb*nw
print(ans)
