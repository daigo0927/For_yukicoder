MOD = 10**9+7
n, m = map(int, input().split())

i = 2
counts = []
while i**2 <= m:
    c = 0
    while m%i == 0:
        m //= i
        c += 1
    if c > 0:
        counts.append(c)
    i += 1
if m > 1:
    counts.append(1)

def combi(p, r):
    f = 1
    r = min(r, p-r)
    for i in range(r):
        f *= (p-i)
        f //= (i+1)
    return f

ans = 1
for c in counts:
    ans = (ans * combi(c+n-1, c))%MOD
print(ans)
