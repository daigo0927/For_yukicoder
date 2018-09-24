n, y = list(map(int, input().split()))

ans = [-1, -1, -1]
for i in range(n+1):
    for j in range(n+1-i):
        k = n-i-j
        if 10000*i + 5000*j + 1000*k == y:
            ans = [i, j, k]
            break
        
print(' '.join(list(map(str, ans))))
