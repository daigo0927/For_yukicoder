h, w = list(map(int, input().split()))
s = [input() for _ in range(h)]

adj = [(1, 0), (0, 1), (-1, 0), (0, -1)]
non_adj = 0
for y in range(h):
    for x in range(w):
        if s[y][x] == '.':
            continue
        n_adj = 0
        for dx, dy in adj:
            i, j = y+dy, x+dx
            if i < 0 or i >= h or j < 0 or j >= w:
                continue
            if s[i][j] == '#':
                n_adj += 1
        if n_adj == 0:
            non_adj += 1
# print(non_adj)
if non_adj == 0:
    print('Yes')
else:
    print('No')
    
