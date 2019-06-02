s = input()

n_win = sum([1 for ss in s if ss == 'o'])
ans = 'YES' if 15-len(s) >= 8-n_win else 'NO'
print(ans)
