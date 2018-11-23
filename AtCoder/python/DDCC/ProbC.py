MOD = 10**9+7
n = int(input())

ans = 0
for i in range(1, n+1):
    p_ways = (pow(i, 10, MOD) - pow((i-1), 10, MOD))%MOD
    q_ways = pow(n//i, 10, MOD)
    # print(p_ways, q_ways)

    ans = (ans + ((p_ways*q_ways)%MOD))%MOD

print(ans)
