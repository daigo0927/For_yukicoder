x = int(input())

sqrt = int(x**(1/2))
ans = 1
for b in range(2, sqrt+1):
    p = 2
    while b**p <= x:
        ans = max(ans, b**p)
        p += 1
print(ans)
