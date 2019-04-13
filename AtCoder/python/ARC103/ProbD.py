n = int(input())
xy = [list(map(int, input().split())) for _ in range(n)]

if len(set([(x+y)%2 for x, y in xy])) > 1:
    print(-1)
    exit()

m = 0
d = []
if sum(xy[0])%2 == 0:
    m += 1
    d.append(1)
for i in range(39):
    m +=1
    d.append(2**i)
print(m)
print(' '.join(list(map(str, d))))

for x, y in xy:
    ans = ''
    for dd in d[::-1]:
        if y >= abs(x): # Up
            ans = 'U' + ans
            y -= dd
        elif y > x and y < -x: # Left
            ans = 'L' + ans
            x += dd
        elif y <= -abs(x): # Down
            ans = 'D' + ans
            y += dd
        else: # Right
            ans = 'R' + ans
            x -= dd
    print(ans)
