n, k = map(int, input().split())
x = list(map(int, input().split()))

ans = 10**18
for i in range(n-k+1):
    x_s, x_e = x[i], x[i+k-1]
    if x_e <= 0:
        ans_tmp = -x_s
    elif x_s < 0 and 0 < x_e:
        ans_tmp = min(x_e-2*x_s, 2*x_e-x_s)
    else:
        ans_tmp = x_e
    ans = min(ans, ans_tmp)
print(ans)
