d, n = map(int, input().split())

if d == 0:
    ans = n if n != 100 else 101
else:
    ans = 100**d*n if n != 100 else 100**d*(n+1)
print(ans)
