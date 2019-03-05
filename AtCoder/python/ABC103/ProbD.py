n, m = map(int, input().split())
ab = [list(map(int, input().split())) for _ in range(m)]

ab = sorted(ab, key = lambda x: x[1])
a_cur = -1
ans = 0
for a, b in ab:
    if a_cur < a:
        ans += 1
        a_cur = b-1
    else:
        pass
print(ans)
