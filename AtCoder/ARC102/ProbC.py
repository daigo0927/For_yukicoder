n, k = map(int, input().split())


ans = (n//k)**3
if k%2 == 0:
    ans += (1 + (n-k//2)//k)**3
print(ans)
