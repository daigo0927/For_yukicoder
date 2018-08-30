n = int(input())
a = list(map(int, input().split()))

sticks = {}
for i in range(n):
    if not a[i] in sticks.keys():
        sticks[a[i]] = 1
    else:
        sticks[a[i]] += 1

edge1, edge2 = 0, 0
lengths = sorted(sticks.keys())[::-1]
for l in lengths:
    if sticks[l] >= 4:
        if edge1 == 0:
            edge1, edge2 = l, l
            break
        else:
            edge2 = l
            break
    elif sticks[l] >= 2:
        if edge1 == 0:
            edge1 = l
        else:
            edge2 = l
            break

print(edge1*edge2)
