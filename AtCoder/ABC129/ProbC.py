MOD = 10**9+7
n, m = map(int, input().split())
a = set([int(input()) for _ in range(m)])

ans = [0]*(n+1)
ans[0] = 1
ans[1] = 1 if not 1 in a else 0
for i in range(2, n+1):
    if i not in a:
        ans[i] = (ans[i-2] + ans[i-1])%MOD
print(ans[-1])
