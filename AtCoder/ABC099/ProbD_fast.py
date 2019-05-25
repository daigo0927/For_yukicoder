from itertools import permutations
n, c = map(int, input().split())
D = [list(map(int, input().split())) for _ in range(c)]
C = [list(map(int, input().split())) for _ in range(n)]

colors = [[0]*c for _ in range(3)]
for i in range(n):
    for j in range(n):
        c_ij = C[i][j]-1
        index = (i+j)%3
        colors[index][c_ij] += 1

costs = [[0]*c for _ in range(3)]
for i in range(3):
    for c_cur in range(c):
        for c_tar in range(c):
            costs[i][c_tar] += D[c_cur][c_tar]*colors[i][c_cur]

ans = 1000*500**2
for c0, c1, c2 in permutations(range(c), 3):
    diff = costs[0][c0] + costs[1][c1] + costs[2][c2]
    ans = min(ans, diff)
print(ans)
