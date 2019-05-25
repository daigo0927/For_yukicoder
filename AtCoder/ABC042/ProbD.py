MOD = 10**9+7

h, w, a, b = list(map(int, input().split()))
ans = 0

facts = [1]
for i in range(1, h+w-1):
    facts.append((i*facts[i-1])%MOD)
# print(facts[:20])
    
def get_path(n, r):
    return (facts[n] * pow(facts[r], MOD-2, MOD)%MOD * pow(facts[n-r], MOD-2, MOD)%MOD) % MOD

y, x = h-a, b+1
while(True):
    path_0 = get_path(y+x-2, x-1)
    path_1 = get_path(h-y+w-x, w-x)
    # print(y, x, path_0, path_1)
    ans += (path_0*path_1)%MOD
    ans %= MOD

    y -= 1
    x += 1
    if y == 0 or x > w:
        break
    
print(ans)
