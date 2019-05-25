n = int(input())
a = list(map(int, input().split()))

a = sorted([aa - i for i, aa in enumerate(a, start = 1)])
b = a[n//2] if n%2 > 0 else (a[n//2-1]+a[n//2])//2
ans = sum([abs(aa - b) for aa in a])
print(ans)
