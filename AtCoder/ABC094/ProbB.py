n, m, x = list(map(int, input().split()))
a = list(map(int, input().split()))

c1, c2 = 0, 0
for i in range(m):
    if a[i] < x:
        c1 += 1
    else:
        c2 += 1
print(min(c1, c2))
