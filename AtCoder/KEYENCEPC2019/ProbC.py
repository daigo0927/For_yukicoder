from copy import deepcopy
n = int(input())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

if sum(a) < sum(b):
    print(-1)
    exit()

diffs = sorted([(ai, bi, ai - bi) for ai, bi in zip(a, b)], key = lambda x: x[2])
# print(diffs)
if diffs[0][2] >= 0:
    print(0)
    exit()

remains = [d for _, _, d in diffs]
idx = 1
remains_changed = deepcopy(remains)
for i, d in enumerate(remains_changed):
    if d >= 0:
        break
    else:
        while d < 0:
            if remains_changed[-idx] >= -d:
                remains_changed[-idx] += d
                d = 0
                remains_changed[i] = 0
            else:
                d += remains_changed[-idx]
                remains_changed[-idx] = 0
                idx += 1
# print(remains)
# print(remains_changed)
ans = 0
for r, rc in zip(remains, remains_changed):
    if r != rc:
        ans += 1
print(ans)
