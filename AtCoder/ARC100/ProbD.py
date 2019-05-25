n = int(input())
a = list(map(int, input().split()))

i, k = 0, 2
ans = sum(a)
p, q, r, s = 0, a[0], a[1], sum(a[2:])
for j in range(1, n-2):
    q += a[j]
    while abs((q-a[i]) - (p+a[i])) < abs(q - p):
        p += a[i]
        q -= a[i]
        i += 1

    r -= a[j]
    while abs((s-a[k]) - (r+a[k])) < abs(s - r):
        r += a[k]
        s -= a[k]
        k += 1

    pqrs = [p, q, r, s]
    ans = min(ans, abs(max(pqrs) - min(pqrs)))
    # print(i, j, k, ans, pqrs)
    
print(ans)
