n, a, b = list(map(int, input().split()))

ans = 0
for m in range(1, n+1):
    digsum = sum(list(map(int, list(str(m)))))
    if digsum >= a and digsum <= b:
        ans += m
print(ans)
