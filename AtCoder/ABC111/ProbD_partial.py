n = int(input())
xy = [list(map(int, input().split())) for _ in range(n)]

parity = (abs(xy[0][0]) + abs(xy[0][1]))%2
for x, y in xy[1:]:
    if (abs(x)+abs(y))%2 != parity:
        print(-1)
        exit()

if parity == 0:
    d = [1]*40
else:
    d = [1]*39
print(len(d))
print(' '.join(list(map(str, d))))

for x, y in xy:
    ans = ''
    if x < 0:
        for i in range(abs(x)):
            ans += 'L'
            if len(ans) > 40:
                break
    else:
        for i in range(x):
            ans += 'R'
            if len(ans) > 40:
                break
    if y < 0:
        for i in range(abs(y)):
            ans += 'D'
            if len(ans) > 40:
                break
    else:
        for i in range(y):
            ans += 'U'
            if len(ans) > 40:
                break
    if len(d) > len(ans):
        for i in range(0, len(d)-len(ans), 2):
            ans += 'UD'
    print(ans)
