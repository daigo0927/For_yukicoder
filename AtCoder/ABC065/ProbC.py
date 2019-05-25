MOD = 10**9+7
n, m = list(map(int, input().split()))

def fact(x):
    val = 1
    for i in range(1, x+1): val = val*i%MOD
    return val

if abs(m-n) > 1:
    print(0)
elif abs(m-n) == 1:
    ans = (fact(n)*fact(m))%MOD
    print(ans)
else:
    ans = (2*fact(n)*fact(m))%MOD
    print(ans)
