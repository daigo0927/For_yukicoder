n = int(input())
a = list(map(int, input().split()))

counts = {4:0, 2:0, 1:0}
for i in range(n):
    if a[i]%4 == 0:
        counts[4] += 1
    elif a[i]%2 == 0:
        counts[2] += 1
    else:
        counts[1] += 1

if counts[2] > 0:
    if counts[4] >= counts[1]:
        print('Yes')
    else:
        print('No')
else:
    if counts[4] >= counts[1]-1:
        print('Yes')
    else:
        print('No')
