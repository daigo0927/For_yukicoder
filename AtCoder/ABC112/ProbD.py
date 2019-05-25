n, m = list(map(int, input().split()))

cands = []
for i in range(1, int(m**(1/2))+1):
    if m%i == 0:
        cands.append(i)
        cands.append(m//i)
cands = sorted(cands, reverse = True)
# print(cands)

for c in cands:
    if m//c >= n:
        print(c)
        break
