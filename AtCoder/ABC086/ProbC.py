n = int(input())
txy = [list(map(int, input().split())) for _ in range(n)]

ans = 'Yes'
t_cur, x_cur, y_cur = 0, 0, 0
for t, x, y in txy:
    d = abs(x-x_cur) + abs(y-y_cur)
    if t-t_cur >= d and ((t-t_cur)-d)%2 == 0:
        t_cur = t
        x_cur = x
        y_cur = y
    else:
        ans = 'No'
        break
    
print(ans)
