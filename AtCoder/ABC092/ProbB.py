n = int(input())
d, x = list(map(int, input().split()))
a = [int(input()) for _ in range(n)]

ans = x
for i in range(n):
    ans += (d-1)//a[i]+1
print(ans)
