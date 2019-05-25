n, m = map(int, input().split())
a = list(map(int, input().split()))

n_use = [0, 2, 5, 5, 4, 5, 6, 3, 7, 6]
dp = [0]+[-float('inf')]*n

for i in range(1, n+1):
    for a_j in a:
        i_prev = i - n_use[a_j]
        if i_prev < 0:
            continue
        else:
            dp[i] = max(dp[i], dp[i_prev]*10+a_j)
# print(dp)
print(dp[-1])
