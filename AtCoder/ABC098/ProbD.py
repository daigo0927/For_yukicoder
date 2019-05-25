n = int(input())
a = list(map(int, input().split()))

r = 0
ans = 0
sum_a = 0
for l in range(n):
    while r < n and sum_a&a[r] == 0:
        sum_a += a[r]
        ans += r-l+1
        r += 1
    sum_a -= a[l]
print(ans)
