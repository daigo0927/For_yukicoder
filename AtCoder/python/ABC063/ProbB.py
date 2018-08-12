def solve():
    s = input()

    strs = {}
    for ss in s:
        if ss in strs.keys():
            print('no')
            return
        else:
            strs[ss] = 1

    print('yes')
    return

solve()
