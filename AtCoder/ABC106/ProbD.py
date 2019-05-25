n, m, q = list(map(int, input().split()))
lr = [list(map(int, input().split())) for _ in range(m)]
pq = [list(map(int, input().split())) for _ in range(q)]

country = [[0]*(n+1) for _ in range(n+1)]
for l, r in lr:
    country[r][l] += 1

cumsum = [[0]*(n+1) for _ in range(n+1)]
for y in range(1, n+1):
    for x in range(1, n+1):
        cumsum[y][x] = country[y][x]+cumsum[y][x-1]
for y in range(1, n+1):
    for x in range(1, n+1):
        cumsum[y][x] += cumsum[y-1][x]
# for cy in cumsum: print(cy)

for p, q in pq:
    ans = cumsum[q][q] - cumsum[q][p-1] - cumsum[p-1][q] + cumsum[p-1][p-1]
    print(ans)
