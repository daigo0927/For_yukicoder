n = int(input())
a = list(map(int, input().split()))

a = sorted([aa - (i+1) for i, aa in enumerate(a)])
if n%2 == 0:
    b = (a[n//2-1] + a[n//2])//2
else:
    b = a[n//2]
    
ans = 0
for i in range(n):
    ans += abs(a[i]-b)
print(ans)
