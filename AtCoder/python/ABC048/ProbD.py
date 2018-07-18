s = input()

ans = 'Second'
idx = 1
while(True):
    if s[idx-1] == s[idx+1] or idx == 0:
        idx += 1
    else:
        s = s[:idx]+s[idx+1:]
        idx -= 1
        if ans == 'First': ans = 'Second'
        else: ans = 'First'
        # print(s, idx)
    if idx == len(s)-1:
        break

print(ans)
    

