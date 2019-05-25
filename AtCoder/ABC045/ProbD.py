from itertools import product

h, w, n = list(map(int, input().split()))
idxs = {}
ans = [0]*10
for i in range(n):
    a, b = list(map(int, input().split()))
    for a_, b_ in product(range(a-1, a+2), range(b-1, b+2)):
        if a_ <= 1 or b_ <= 1 or a_ >= h or b_ >= w:
            continue

        # print(a_, b_)
        if (a_, b_) not in idxs.keys():
            idxs[(a_, b_)] = 1
        else:
            idxs[(a_, b_)] += 1
        
for keys, item in idxs.items():
    ans[item] += 1
ans[0] = (h-2)*(w-2)-sum(ans[1:])

for a in ans:
    print(a)
