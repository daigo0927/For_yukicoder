n, x = list(map(int, input().split()))
m = [int(input()) for _ in range(n)]

ans = n
x -= sum(m)
mmin = min(m)
ans += x//mmin
print(ans)
