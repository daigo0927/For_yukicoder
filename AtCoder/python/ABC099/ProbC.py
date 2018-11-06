n = int(input())

cands = [1]
for i in range(1, 10):
    if 6**i <= 100000:
        cands.append(6**i)
    if 9**i <= 100000:
        cands.append(9**i)
cands = sorted(cands)
# print(cands)

ans = list(range(n+1))
for c in cands[1:]:
    for i in range(n+1):
        if i < c:
            pass
        else:
            ans[i] = min(ans[i], ans[i-c] + 1)
print(ans[-1])
