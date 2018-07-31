n, m = list(map(int, input().split()))
ab = [list(map(int, input().split())) for _ in range(n)]
cd = [list(map(int, input().split())) for _ in range(m)]

for a, b in ab:
    min_dist = 4*10**8+1
    for i, (c, d) in enumerate(cd):
        dist = abs(a-c)+abs(b-d)
        if dist < min_dist:
            min_dist = dist
            ans = i+1
    print(ans)

