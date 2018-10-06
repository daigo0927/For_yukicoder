n, T = list(map(int, input().split()))
ans = 10000
for i in range(n):
    c, t = list(map(int, input().split()))
    if t > T:
        continue
    else:
        ans = min(ans, c)
if ans == 10000:
    print('TLE')
else:
    print(ans)
