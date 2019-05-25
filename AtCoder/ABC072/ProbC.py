n = int(input())
a = list(map(int, input().split()))

num = {}
for i in range(n):
    if not a[i] in num.keys():
        num[a[i]] = 1
    else:
        num[a[i]] += 1
    if not a[i]-1 in num.keys():
        num[a[i]-1] = 1
    else:
        num[a[i]-1] += 1
    if not a[i]+1 in num.keys():
        num[a[i]+1] = 1
    else:
        num[a[i]+1] += 1

ans = 0
for k in num.keys():
    ans = max(ans, num[k])
print(ans)
