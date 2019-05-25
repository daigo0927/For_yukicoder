n = int(input())
s = input()

n_e = 0
for ss in s:
    if ss == 'E':
        n_e += 1
n_w = n - n_e

n_change_left = 0
n_change_right = n_e-1 if s[0] == 'E' else n_e
ans = n_change_left + n_change_right
for i in range(1, n):
    if s[i-1] == 'W':
        n_change_left += 1
    if s[i] == 'E':
        n_change_right -= 1
    ans = min(ans, n_change_left+n_change_right)
print(ans)
