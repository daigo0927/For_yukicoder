n = int(input())
a = list(map(int, input().split()))

ans = []

a_min = 10**6+1
a_max = -(10**6+1)
for i in range(n):
    if a[i] > a_max:
        a_max = a[i]
        i_max = i
    if a[i] < a_min:
        a_min = a[i]
        i_min = i

if a_max > abs(a_min):
    for i in range(n):
        if a[i] < 0:
            a[i] += a_max
            ans.append(str(i_max+1)+' '+str(i+1))
    for i in range(1, n):
        a[i] += a[i-1]
        ans.append(str(i)+' '+str(i+1))
else:
    for i in range(n):
        if a[i] > 0:
            a[i] -= a_min
            ans.append(str(i_min+1)+' '+str(i+1))
    for i in range(n-2, -1, -1):
        a[i] += a[i+1]
        ans.append(str(i+2)+' '+str(i+1))

print(len(ans))
for i in range(len(ans)):
    print(ans[i])
                

    
