n, a = list(map(int, input().split()))
x = list(map(int, input().split()))
max_x = max(max(x), a)
x = [-10**6] + [xx-a for xx in x]
dp = [[0]*(2*n*max_x+1) for _ in range(n+1)]
dp[0][n*max_x] = 1

# import numpy as np
# print(np.shape(dp))

for i in range(1, n+1):
    for j in range(2*n*max_x+1):
        if j-x[i] < 0 or j-x[i] > 2*n*max_x:
            dp[i][j] = dp[i-1][j]
        elif j-x[i] >= 0 and j-x[i] <= 2*n*max_x:
            dp[i][j] = dp[i-1][j] + dp[i-1][j-x[i]]

# print(np.array(dp))
print(dp[n][n*max_x]-1)
        
