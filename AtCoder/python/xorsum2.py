N = int(input())
A = list(map(int, input().split(' ')))

r = 0
ans = 0
tmp = 0
for l in range(N):
    while r < N and tmp&A[r] == 0:
        tmp = tmp|A[r]
        r += 1
    ans += r-l
    print(l, r)
    tmp = tmp^A[l]
    
print(ans)
