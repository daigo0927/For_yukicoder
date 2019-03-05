n, m = map(int, input().split())
ab = [list(map(int, input().split())) for _ in range(m)]

ends = [[[], []] for _ in range(n+1)]
for i, (a, b) in enumerate(ab, start = 1):
    ends[a][0].append(i)
    ends[b][1].append(i)
# for e in ends: print(e)

ans = 0
orders = set([])
for start, end in ends:
    if len(end) > 0:
        rm_bridge = False
        for e in end:
            if e in orders:
                orders.remove(e)
                rm_bridge = True
        if rm_bridge:
            orders = set([])
        ans += int(rm_bridge)
    if len(start) > 0:
        for s in start:
            orders.add(s)
    # print(orders)
print(ans)
