h, w = list(map(int, input().split()))
a = [list(map(int, input().split())) for i in range(h)]

ans = []
for i in range(h):
    for j in range(w):
        if i == h-1 and j == w-1:
            continue
        if a[i][j]%2 == 0:
            continue
        else:
            if j < w-1 and a[i][j+1]%2 == 1:
                a[i][j] -= 1
                a[i][j+1] += 1
                ans.append([i+1, j+1, i+1, j+2])
                continue
            elif i < h-1 and a[i+1][j]%2 == 1:
                a[i][j] -= 1
                a[i+1][j] += 1
                ans.append([i+1, j+1, i+2, j+1])
                continue
            if j < w-1:
                a[i][j] -= 1
                a[i][j+1] += 1
                ans.append([i+1, j+1, i+1, j+2])
                continue
            elif i < h-1:
                a[i][j] -= 1
                a[i+1][j] += 1
                ans.append([i+1, j+1, i+2, j+1])
                continue

# for i in range(h): print(a[i])
print(len(ans))
for i in range(len(ans)):
    print(' '.join(list(map(str, ans[i]))))
