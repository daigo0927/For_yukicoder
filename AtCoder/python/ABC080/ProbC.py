n = int(input())
f = [list(map(int, input().split())) for _ in range(n)]
p = [list(map(int, input().split())) for _ in range(n)]

ans = -10**10
for bit in range(1, 1<<10):
    score = 0
    for i in range(n):
        time = 0
        for t in range(10):
            if bit&(1<<t) and f[i][t] == 1:
                time += 1
        score += p[i][time]
    ans = max(ans, score)

print(ans)
