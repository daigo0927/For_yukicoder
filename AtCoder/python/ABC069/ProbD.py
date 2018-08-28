h, w = list(map(int, input().split()))
n = int(input())
a = [0]+list(map(int, input().split()))

ans = [[0]*w for _ in range(h)]
color = 1
for y in range(h):
    for x in range(w):
        if y%2 == 0:
            ans[y][x] = color
        else:
            ans[y][-(x+1)] = color
        a[color] -= 1
        if a[color] == 0:
            color += 1

    print(' '.join(map(str, ans[y])))
