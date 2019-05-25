s = input()
x, y = list(map(int, input().split()))

s = s.split('T')
move_x = s[::2]
move_y = s[1::2]

x_cur = len(move_x[0])
for nx in sorted(move_x[1:], reverse = True):
    if x_cur <= x:
        x_cur += len(nx)
    else:
        x_cur -= len(nx)

y_cur = 0
for ny in sorted(move_y, reverse = True):
    if y_cur <= y:
        y_cur += len(ny)
    else:
        y_cur -= len(ny)

if x_cur == x and y_cur == y:
    print('Yes')
else:
    print('No')
