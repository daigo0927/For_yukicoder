n, m = list(map(int, input().split()))
ans = dict(zip(range(1, n+1), [0]*n))
for _ in range(m):
    a, b = list(map(int, input().split()))
    ans[a] += 1
    ans[b] += 1

for i in range(1, n+1):
    print(ans[i])
