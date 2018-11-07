n, m = map(int, input().split())
xyz = [list(map(int, input().split())) for _ in range(n)]

if m == 0:
    print(0)
    exit()

ans = 0
for i in range(1<<3):
    x = [w[0] if i&1 > 0 else -w[0] for w in xyz]
    y = [w[1] if i&2 > 0 else -w[1] for w in xyz]
    z = [w[2] if i&4 > 0 else -w[2] for w in xyz]
    sums = [xx+yy+zz for xx, yy, zz in zip(x, y, z)]
    sums = sorted(sums, reverse = True)
    ans = max(ans, sum(sums[:m]))
print(ans)
