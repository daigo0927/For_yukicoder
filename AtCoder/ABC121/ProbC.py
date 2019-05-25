n, m = map(int, input().split())
drinks = [list(map(int, input().split())) for _ in range(n)]

drinks = sorted(drinks, key = lambda x: x[0])
ans = 0
for a, b in drinks:
    if b < m:
        ans += a*b
    elif b == m:
        ans += a*b
        break
    else:
        ans += a*m
        break
    m -= b
print(ans)
