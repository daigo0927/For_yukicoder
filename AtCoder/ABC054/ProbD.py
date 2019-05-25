ABMAX = 10
L = 10**6

n, ma, mb = list(map(int, input().split()))
a, b, c = [0]*n, [0]*n, [0]*n
for i in range(n):
    a[i], b[i], c[i] = list(map(int, input().split()))

dp = [[[L for cb in range(n*ABMAX+1)] for ca in range(n*ABMAX+1)] for i in range(n+1)]
dp[0][0][0] = 0

for i in range(n):
    for ca in range(n*ABMAX+1):
        for cb in range(n*ABMAX+1):
            if dp[i][ca][cb] == L:
                continue
            
            dp[i+1][ca][cb] = min(dp[i+1][ca][cb], dp[i][ca][cb])
            dp[i+1][ca+a[i]][cb+b[i]] = min(dp[i+1][ca+a[i]][cb+b[i]],
                                            dp[i][ca][cb]+c[i])

ans = L
for ca in range(1, n*ABMAX):
    for cb in range(1, n*ABMAX):
        if ca*mb == cb*ma:
            ans = min(ans, dp[n][ca][cb])

if ans == L: print(-1)
else: print(ans)
                
