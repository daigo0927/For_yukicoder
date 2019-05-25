MOD = 10**9+7
s = input()

dp = [[0]*4 for _ in range(len(s)+1)]
dp[0][0] = 1
for i, ss in enumerate(s):
    if ss == 'A':
        dp[i+1][0] = dp[i][0]
        dp[i+1][1] = (dp[i][1] + dp[i][0])%MOD
        dp[i+1][2] = dp[i][2]
        dp[i+1][3] = dp[i][3]
    elif ss == 'B':
        dp[i+1][0] = dp[i][0]
        dp[i+1][1] = dp[i][1]
        dp[i+1][2] = (dp[i][2] + dp[i][1])%MOD
        dp[i+1][3] = dp[i][3]
    elif ss == 'C':
        dp[i+1][0] = dp[i][0]
        dp[i+1][1] = dp[i][1]
        dp[i+1][2] = dp[i][2]
        dp[i+1][3] = (dp[i][3] + dp[i][2])%MOD
    else:
        dp[i+1][0] = dp[i][0]*3%MOD
        dp[i+1][1] = (dp[i][1]*3%MOD + dp[i][0])%MOD
        dp[i+1][2] = (dp[i][2]*3%MOD + dp[i][1])%MOD
        dp[i+1][3] = (dp[i][3]*3%MOD + dp[i][2])%MOD

# for dp_ in dp: print(dp_)
print(dp[-1][3])
