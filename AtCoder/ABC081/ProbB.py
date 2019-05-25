n = int(input())
a = list(map(int, input().split()))

ans = 0
done = False
while not done:
    for i in range(n):
        if a[i]%2 == 0:
            a[i] = a[i]/2
        else:
            done = True
            break
    if not done:
        ans += 1
print(ans)
