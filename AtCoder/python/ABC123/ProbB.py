a = [int(input()) for _ in range(5)]

ans = 0
b = []
for aa in a:
    if aa%10 == 0:
        ans += aa
    else:
        b.append((aa, aa%10))
if len(b) > 0:
    b = sorted(b, key = lambda x: x[1], reverse = True)
    ans += sum([10*(bb//10+1) for bb, _ in b[:-1]])
    ans += b[-1][0]
print(ans)
