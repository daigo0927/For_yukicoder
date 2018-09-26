n = int(input())
a = [list(map(int, input().split())) for _ in range(2)]

sum_cur = a[0][0] + sum(a[1])
ans = sum_cur
for i in range(1, n):
    sum_cur = sum_cur+a[0][i]-a[1][i-1]
    ans = max(ans, sum_cur)
print(ans)
