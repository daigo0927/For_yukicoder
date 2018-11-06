from itertools import permutations
n, c = map(int, input().split())
D = [list(map(int, input().split())) for _ in range(c)]
C = [list(map(int, input().split())) for _ in range(n)]

colors = [[0]*c for _ in range(3)]
for i in range(n):
    for j in range(n):
        c_ij = C[i][j]-1
        index = (i+j)%3
        for col in range(c):
            colors[index][col] += D[c_ij][col]

ans = 1000*500**2
for c0, c1, c2 in permutations(range(c), 3):
    diff = colors[0][c0] + colors[1][c1] + colors[2][c2]
    ans = min(ans, diff)
print(ans)
