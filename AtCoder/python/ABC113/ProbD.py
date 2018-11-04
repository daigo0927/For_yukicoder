MOD = 10**9+7
h, w, k = map(int, input().split())

dp = [[0]*w for _ in range(h+1)]
dp[0][0] = 1

patterns = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55]

if w == 1:
    print(1)
    exit()

for i in range(1, h+1):
    # most left
    dp[i][0] = (dp[i-1][0]*patterns[1:][w-2]%MOD + dp[i-1][1]*patterns[w-2]%MOD)%MOD
    for j in range(1, w-1):
        npath = dp[i-1][j-1]*(patterns[j-1]*patterns[1:][w-j-2])%MOD\
                + dp[i-1][j]*(patterns[1:][j-1]*patterns[1:][w-j-2])%MOD\
                + dp[i-1][j+1]*(patterns[1:][j-1]*patterns[w-j-2])%MOD
        dp[i][j] = npath%MOD
    dp[i][w-1] = (dp[i-1][w-2]*patterns[w-2]%MOD + dp[i-1][w-1]*patterns[1:][w-2]%MOD)%MOD

# for p in dp: print(p)

print(dp[-1][k-1])
    
