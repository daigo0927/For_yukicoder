n, m = map(int, input().split())
ks = []
for i in range(m):
    inp = list(map(int, input().split()))
    ks.append(inp[1:])
p = list(map(int, input().split()))

ans = 0
for i in range(1<<n):
    on_all = True
    for j in range(m):
        n_on = 0
        for s in ks[j]:
            if i&(1<<(s-1)):
                n_on += 1
        if not n_on%2 == p[j]:
            on_all = False
    if on_all:
        ans += 1
print(ans)
