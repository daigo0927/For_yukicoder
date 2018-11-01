n = int(input())
s = input()

ans = 0
for i in range(1, n):
    x1 = set(s[:i])
    x2 = set(s[i:])
    ans_cur = 0
    for xx1 in x1:
        if xx1 in x2:
            ans_cur +=1
    ans = max(ans, ans_cur)
print(ans)
