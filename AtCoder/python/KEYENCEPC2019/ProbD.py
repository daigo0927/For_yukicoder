MOD = 10**9+7
n, m = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

if len(set(a)) < n or len(set(b)) < m:
    print(0)
    exit()
if max(a) != n*m or max(b) != n*m:
    print(0)
    exit()

a = sorted(a, reverse = True)
b = sorted(b, reverse = True)
i, j = 0, 0
ans = 1
for num in range(n*m, 0, -1):
    while i < n-1 and a[i+1] >= num:
        i += 1
    while j < m-1 and b[j+1] >= num:
        j += 1
        
    if a[i] == num and b[j] == num:
        pass
    elif a[i] == num:
        ans = (ans*(j+1))%MOD
    elif b[j] == num:
        ans = (ans*(i+1))%MOD
    else:
        cand = max((i+1)*(j+1) - (n*m - num), 0)
        ans = (ans*cand)%MOD
print(ans)
    
