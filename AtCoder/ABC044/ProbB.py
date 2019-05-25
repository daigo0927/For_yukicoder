w = input()
d = {}
for ww in w:
    if ww not in d.keys():
        d[ww] = 1
    else:
        d[ww] += 1

def solve(d):
    for key, item in d.items():
        if item%2 == 1:
            print('No')
            return
        
    print('Yes')
    return

solve(d)

