n, x = list(map(int, input().split()))
a = list(map(int, input().split()))

ans = 0
for i in range(1, n):
    if a[i]+a[i-1] > x:
        eat = min(a[i]+a[i-1]-x, a[i])
        ans += eat
        a[i] -= eat
    if a[i]+a[i-1] > x:
        eat = min(a[i]+a[i-1]-x, a[i-1])
        ans += eat
        a[i-1] -= eat

print(ans)

