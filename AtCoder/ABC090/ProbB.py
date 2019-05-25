a, b = list(map(int, input().split()))

ans = 0
for n in range(a, b+1):
    n = str(n)
    if n[0] == n[-1] and n[1] == n[-2]:
        ans += 1
print(ans)
