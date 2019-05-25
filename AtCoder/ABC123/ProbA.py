a = [int(input()) for _ in range(5)]
k = int(input())

ans = 'Yay!'
for i in a:
    for j in a:
        if abs(i - j) > k:
            ans = ':('
print(ans)
