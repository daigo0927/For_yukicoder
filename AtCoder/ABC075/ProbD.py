n, k = list(map(int, input().split()))
xy = [list(map(int, input().split())) for _ in range(n)]

xy = sorted(xy)
ans = 4*10**18
for i in range(n-k+1):
    x_left = xy[i][0]
    for j in range(i+k-1, n):
        x_right = xy[j][0]
        y_mid = sorted([y for x, y in xy[i:j+1]])
        for k_ in range(len(y_mid)-k+1):
            y_bottom = y_mid[k_]
            y_top = y_mid[k_+k-1]
            ans = min(ans, (x_right-x_left)*(y_top-y_bottom))
print(ans)
