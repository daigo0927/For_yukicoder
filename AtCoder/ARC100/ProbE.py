n = int(input())
a = list(map(int, input().split()))

dp = [(0, 0, a[0]), (0, 1, sum(a[:2]))]

print(dp[1][2])
power = 0
pow2 = [2**p for p in range(19)]
for i in range(2, 2**n):
    if i == pow2[power+1]:
        power += 1

    i_0 = i-pow2[power]
    i_00, i_01, ans_0 = dp[i_0]
    
    i_1 = i&(i-1)
    i_10, i_11, ans_1 = dp[i_1]
    _, _, ans_prev = dp[i-1]

    a_tops = set([(a[i_00], i_00), (a[i_01], i_01),
                  (a[i_10], i_10), (a[i_11], i_11),
                  (a[i], i)])
    a_top1, a_top2 = sorted(a_tops, reverse = True)[:2]
    ans = max(a_top1[0]+a_top2[0], ans_prev)
    print(ans)
    dp.append((a_top1[1], a_top2[1], ans))
    
# print(dp)
