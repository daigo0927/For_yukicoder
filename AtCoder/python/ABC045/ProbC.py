from copy import deepcopy
s = input()
length = len(s)

ans = 0
def solve(s_split, s, i):
    if i == length:
        # print(s_split)
        global ans
        ans += sum(list(map(int, s_split)))
    else:
        tmp1 = deepcopy(s_split)
        tmp1[-1] += s[0]
        solve(tmp1, s[1:], i+1)

        tmp2 = deepcopy(s_split)
        tmp2.append(s[0])
        solve(tmp2, s[1:], i+1)
        
solve([s[0]], s[1:], 1)
print(ans)


