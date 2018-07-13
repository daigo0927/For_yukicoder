s = input()
ans = ''
for ss in s:
    if ss == '0':
        ans += '0'
    elif ss == '1':
        ans += '1'
    else:
        ans = ans[:-1]
print(ans)
