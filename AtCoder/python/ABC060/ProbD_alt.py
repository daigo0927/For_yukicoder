from collections import defaultdict
n, W = list(map(int, input().split()))
wv = [list(map(int, input().split())) for _ in range(n)]

dp = defaultdict(int)
dp[0] = 0
for w, v in wv:
    dp_cur = list(dp.items())
    for w_cur, v_cur in dp_cur:
        if w_cur+w <= W:
            dp[w_cur+w] = max(dp[w_cur+w], v_cur+v)

# print(dp)
print(max(dp.values()))
