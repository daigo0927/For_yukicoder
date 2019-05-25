n = int(input())
p = list(map(int, input().split()))

ans = 0
for i in range(n):
    if p[i] == i+1:
        tmp = p[i]
        if i < n-1:
            p[i] = p[i+1]
            p[i+1] = tmp
        else:
            p[i] = p[i-1]
            p[i-1] = tmp
        ans += 1

print(ans, p)
