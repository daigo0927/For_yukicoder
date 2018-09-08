a, b = list(map(int, input().split()))

ans = 'No'
for c in [1,2,3]:
    if (a*b*c)%2 == 1:
        ans = 'Yes'
        break
print(ans)
