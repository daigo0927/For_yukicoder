s = input()

ans = 0
for ss in s:
    ans += 1 if ss == '+' else -1
print(ans)
