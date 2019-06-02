import sys
input = sys.stdin.readline
MOD = 10**6+3
q = int(input())

fact = [1]*MOD
for i in range(1, MOD):
    fact[i] = fact[i-1]*i%MOD

for _ in range(q):
    x, d, n = map(int, input().split())
    if d == 0:
        ans = pow(x, n, MOD)
    else:
        x_div = x*pow(d, MOD-2, MOD)%MOD
        if x_div+n-1 > MOD:
            ans = 0
        else:
            if x_div+n-1 >= MOD:
                ans = 0
            else:
                f = fact[x_div+n-1]
                fi = pow(fact[x_div-1], MOD-2, MOD)
                ans = f*fi%MOD*pow(d, n, MOD)%MOD
    print(ans)
