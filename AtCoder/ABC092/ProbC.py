n = int(input())
a = list(map(int, input().split()))

d, d_skip = [0], [0]
for i in range(n):
    if i == 0:
        d.append(abs(a[i]))
    else:
        d.append(abs(a[i]-a[i-1]))
d.append(abs(a[-1]))

for i in range(n):
    if i == 0:
        d_skip.append(abs(a[i+1]))
    elif i < n-1:
        d_skip.append(abs(a[i+1] - a[i-1]))
    else:
        d_skip.append(abs(a[i-1]))

d_cumsum = [0]
for d_i in d[1:]:
    d_cumsum.append(d_i+d_cumsum[-1])
# print(d_cumsum, d_skip)
for i in range(1, n+1):
    ans = d_cumsum[i-1] + d_skip[i] + (d_cumsum[-1] - d_cumsum[i+1])
    print(ans)
    
