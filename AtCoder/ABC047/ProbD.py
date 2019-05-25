n, t = list(map(int, input().split()))
a = list(map(int, input().split()))

remain_max = [a[-1]]*n
for i in range(1, n):
    remain_max[-(i+1)] = max(a[-i], remain_max[-i])

diffs = [0]*n
for i in range(n):
    diffs[i] = remain_max[i] - a[i]

max_diff = 0
ans = 0
for i in range(n):
    if diffs[i] > max_diff:
        max_diff = diffs[i]
        ans = 1
    elif diffs[i] == max_diff:
        ans += 1
        
# print(diffs, ans)
print(ans)

