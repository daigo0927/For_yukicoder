n = input()

sgs = ['7', '5', '3']
cands = {3:[]}
for i in sgs:
    for j in sgs:
        for k in sgs:
            cands[3].append(i+j+k)
for d in range(4, 10):
    cands[d] = []
    for cand in cands[d-1]:
        for i in sgs:
            cands[d].append(cand+str(i))
# print(cands)
ans = 0
for d, value in cands.items():
    for v in value:
        if int(v) <= int(n) and len(set(list(v))) == 3:
            ans += 1
print(ans)
