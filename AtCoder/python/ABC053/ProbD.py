n = int(input())
a = list(map(int, input().split()))

a_n = {}
for i in range(n):
    if a[i] not in a_n.keys():
        a_n[a[i]] = 1
    else:
        a_n[a[i]] += 1

if (n-len(a_n.keys()))%2 == 0:
    print(len(a_n.keys()))
else:
    print(len(a_n.keys())-1)
