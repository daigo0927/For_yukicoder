n, k = map(int, input().split())
v = list(map(int, input().split()))

ans = 0
for lr in range(min(n, k)+1):
    for l in range(lr+1):
        r = lr - l
        jewels = v[:l]+v[-r:] if r > 0 else v[:l]
        n_release = k - lr
        ans_cur = 0
        for j in sorted(jewels):
            if j < 0 and n_release > 0:
                n_release -= 1
            else:
                ans_cur += j
        ans = max(ans, ans_cur)
        
print(ans)
