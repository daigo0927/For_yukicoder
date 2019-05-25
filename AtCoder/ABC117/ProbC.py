n, m = map(int, input().split())
x = list(map(int, input().split()))

x = sorted(x)
mid = [x[i+1]-x[i] for i in range(m-1)]
mid = sorted(mid)
ans = sum(mid) if n == 1 else sum(mid[:-(n-1)])
print(ans)
