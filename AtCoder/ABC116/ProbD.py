n, k = map(int, input().split())
td = [list(map(int, input().split())) for _ in range(n)]

td = sorted(td, key = lambda x: x[1], reverse = True)
eat_types = set()
sushi_dup = []
value = 0
for t, d in td[:k]:
    if not t in eat_types:
        eat_types.add(t)
    else:
        sushi_dup.append(d)
    value += d

ans = value + len(eat_types)**2
for t, d in td[k:]:
    if len(sushi_dup) == 0:
        break
    
    if t in eat_types:
        continue
    else:
        eat_types.add(t)
        r = sushi_dup.pop()
        value += d - r
        ans = max(ans, value + len(eat_types)**2)
print(ans)
