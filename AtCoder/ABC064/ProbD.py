n = int(input())
s = input()

ans = s
n_left, n_right = 0, 0
for ss in s:
    if ss == '(':
        n_left += 1
    else:
        if n_left > 0:
            n_left -= 1
        else:
            ans = '('+ans
if n_left > 0:
    for _ in range(n_left): ans += ')'

print(ans)
