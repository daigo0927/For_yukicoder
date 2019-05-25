w, h, n = list(map(int, input().split()))
rect = [[1]*h for _ in range(w)]

for _ in range(n):
    x, y, a = list(map(int, input().split()))
    if a == 1:
        for xx in range(x):
            for yy in range(h):
                rect[xx][yy] = 0
    elif a == 2:
        for xx in range(x, w):
            for yy in range(h):
                rect[xx][yy] = 0
    elif a == 3:
        for xx in range(w):
            for yy in range(y):
                rect[xx][yy] = 0
    else:
         for xx in range(w):
             for yy in range(y, h):
                 rect[xx][yy] = 0

ans = 0
for xx in range(w):
    for yy in range(h):
        ans += rect[xx][yy]

print(ans)
