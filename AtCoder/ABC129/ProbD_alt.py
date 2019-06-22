# Can pass with PyPy3
h, w = map(int, input().split())
s = [input() for _ in range(h)]

hdots = [[0]*(w+1) for _ in range(h)]
for j in range(h):
    ndots = 0
    for i in range(1, w+1):
        if s[j][i-1] == '.':
            ndots += 1
        else:
            hdots[j][i-1] = ndots
            ndots = 0
    hdots[j][-1] = ndots if s[j][-1] == '.' else 0
    for i in range(w, 0, -1):
        if s[j][i-1] == '.':
            hdots[j][i] = ndots
        else:
            ndots = hdots[j][i-1]
vdots = [[0]*w for _ in range(h+1)]
for i in range(w):
    ndots = 0
    for j in range(1, h+1):
        if s[j-1][i] == '.':
            ndots += 1
        else:
            vdots[j-1][i] = ndots
            ndots = 0
    vdots[-1][i] = ndots if s[-1][i] == '.' else 0
    for j in range(h, 0, -1):
        if s[j-1][i] == '.':
            vdots[j][i] = ndots
        else:
            ndots = vdots[j-1][i]
            
ans = 0
for j in range(h):
    for i in range(w):
        nh, nv = hdots[j][i+1], vdots[j+1][i]
        if nh == 0 or nv == 0:
            continue
        ans = max(ans, nh+nv-1)
print(ans)
