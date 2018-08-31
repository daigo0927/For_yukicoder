n = int(input())
a = [int(input()) for _ in range(n)]

num = {}
for i in range(n):
    if not a[i] in num.keys():
        num[a[i]] = 1
    elif num[a[i]] == 1:
        num[a[i]] = 0
    else:
        num[a[i]] = 1
        
ans = 0
for k in num.keys():
    if num[k] > 0:
        ans += 1
print(ans)
