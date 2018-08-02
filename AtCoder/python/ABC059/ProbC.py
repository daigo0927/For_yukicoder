n = int(input())
a = list(map(int, input().split()))

answers = []
for p in [True, False]:
    ans = 0
    cumsum = 0
    for i in range(n):
        if p:
            if cumsum+a[i] >= 0:
                ans += cumsum+a[i]+1
                cumsum = -1
            else:
                cumsum += a[i]
            p = False
        else:
            if cumsum+a[i] <= 0:
                ans += 1-(cumsum+a[i])
                cumsum = 1
            else:
                cumsum += a[i]
            p = True
        # print(cumsum)
    answers.append(ans)
    
print(min(answers))
