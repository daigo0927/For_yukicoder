n, m = map(int, input().split())
count = dict(zip(range(1, m+1), [0]*m))
for _ in range(n):
    ka = list(map(int, input().split()))
    for a in ka[1:]:
        count[a] += 1

ans = sum([1 for k, v in count.items() if v == n])
print(ans)
