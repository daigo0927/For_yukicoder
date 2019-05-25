sx, sy, tx, ty = list(map(int, input().split()))

ans = 'L'
for _ in range(ty-sy+1): ans += 'U'
for _ in range(tx-sx+1): ans += 'R'
ans += 'DR'
for _ in range(ty-sy+1): ans += 'D'
for _ in range(tx-sx+1): ans += 'L'
ans += 'U'

for _ in range(ty-sy): ans += 'U'
for _ in range(tx-sx): ans += 'R'
for _ in range(ty-sy): ans += 'D'
for _ in range(tx-sx): ans += 'L'

print(ans)
