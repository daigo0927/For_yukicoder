n = int(input())
a = list(map(int, input().split()))

ans = [0]*n
for i in range(n):
    if i%2 == 0:
        ans[i//2] = str(a[-i-1])
    else:
        ans[n-1-i//2] = str(a[-i-1])
print(' '.join(ans))
