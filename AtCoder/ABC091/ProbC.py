n = int(input())
ab = [tuple(map(int, input().split())) for _ in range(n)]
cd = [tuple(map(int, input().split())) for _ in range(n)]

cd_cands = {}
for c, d in cd:
    cands = []
    for a, b in ab:
        if a < c and b < d:
            cands.append((a, b))
    cd_cands[(c, d)] = cands

cd = sorted(cd, key = lambda x: x[0])
ab_set = set(ab)
ans = 0
for c, d in cd:
    cands = cd_cands[(c, d)]
    if len(cands) == 0:
        continue
    cands = sorted(cands, key = lambda x: x[1], reverse = True)
    for cand in cands:
        if cand in ab_set:
            ans += 1
            ab_set.remove(cand)
            break
print(ans)
        
