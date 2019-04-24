n, k = map(int, input().split())
x = list(map(int, input().split()))

ans = 10**18
for i in range(n-k+1):
    ans = min(ans, min(abs(x[i]-x[i+k-1])+abs(x[i+k-1]), abs(x[i])+abs(x[i]-x[i+k-1])))
print(ans)
