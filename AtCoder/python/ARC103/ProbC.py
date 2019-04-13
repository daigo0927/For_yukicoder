from collections import defaultdict
n = int(input())
v = list(map(int, input().split()))

v1, v2 = defaultdict(int), defaultdict(int)
for i, vv in enumerate(v):
    if i%2 == 0:
        v1[vv] += 1
    else:
        v2[vv] += 1
v1 = sorted([(c, vv) for vv, c in v1.items()], reverse = True)
v2 = sorted([(c, vv) for vv, c in v2.items()], reverse = True)

if v1[0][1] == v2[0][1]:
    if len(v1) == 1 and len(v2) == 1:
        ans = n//2
    elif v1[1][0] > v2[1][0]:
        ans = n - v1[1][0] - v2[0][0]
    else:
        ans = n - v1[0][0] - v2[1][0]
else:
    ans = n - v1[0][0] - v2[0][0]
print(ans)
