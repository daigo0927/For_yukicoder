n = int(input())
xyh = [list(map(int, input().split())) for _ in range(n)]
xyh = sorted(xyh, reverse = True, key = lambda z: z[2])
# print(xyh)

for i in range(101):
    for j in range(101):
        x_0, y_0, h_0 = xyh[0]
        H = h_0 + abs(y_0-i) + abs(x_0-j)
        valid = True
        for x, y, h in xyh[1:]:
            if max(H-abs(y-i)-abs(x-j), 0) != h:
                valid = False
                break
        if valid:
            ans = str(j)+' '+str(i)+' '+str(H)
            print(ans)
            exit()
