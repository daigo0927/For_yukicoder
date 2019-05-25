n, m = map(int, input().split())
a = list(map(int, input().split()))
bc = []
for _ in range(m):
    b, c = map(int, input().split())
    bc.append((b, c))

a = sorted(a)
bc = sorted(bc, key = lambda x: x[1], reverse = True)
i_bc = 0
for i, aa in enumerate(a):
    b, c = bc[i_bc]
    if aa < c:
        a[i] = c
        b -= 1
        bc[i_bc] = (b, c)
        if b == 0:
            i_bc += 1
    if i_bc >= m:
        break
print(sum(a))
