S = input()

ans = 0
ans_cur = 0
for s in S:
    if s in ['A', 'C', 'G', 'T']:
        ans_cur += 1
    else:
        ans = max(ans, ans_cur)
        ans_cur = 0
ans = max(ans, ans_cur)
print(ans)
