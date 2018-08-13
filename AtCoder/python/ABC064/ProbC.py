import copy
n = int(input())
a = list(map(int, input().split()))

color = [0]*9
for i in range(n):
    rate = min(a[i]//400, 8)
    color[rate] += 1

ans_min = 0
color_min = copy.deepcopy(color)
for c in color_min[:-1]:
    if c > 0:
        ans_min += 1
ans_min = max(1, ans_min)

ans_max = 0
color_max = copy.deepcopy(color)
for c in color_max[:-1]:
    if c > 0:
        ans_max += 1
ans_max += color_max[-1]

print(ans_min, ans_max)
