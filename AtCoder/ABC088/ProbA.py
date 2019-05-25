n = int(input())
a = int(input())

ans = 'No'
for i in range(a+1):
    if (n-i)%500 == 0:
        ans = 'Yes'
        break
print(ans)
