n, k = map(int, input().split())

ans = 0
for i in range(1, n+1):
    prob = 1/n
    while i < k:
        i *= 2
        prob /= 2
    ans += prob
print(ans)
