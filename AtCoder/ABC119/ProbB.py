n = int(input())

ans = 0
for _ in range(n):
    x, u = input().split()
    ans += float(x) if u == 'JPY' else float(x)*380000
print(ans)
