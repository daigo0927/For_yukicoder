MOD = 10**9+7
l = input()

dp = [2, 1]
for i in range(1, len(l)):
    x, y = dp
    if l[i] == '1':
        x, y = 2*x%MOD, (x + 3*y%MOD)%MOD
    else:
        x, y = x, 3*y%MOD
    dp = [x, y]
print(sum(dp)%MOD)
