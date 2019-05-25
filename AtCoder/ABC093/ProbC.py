a, b, c = list(map(int, input().split()))
a, b, c = sorted([a, b, c])

if (b-a)%2 == 0:
    ans = (b-a)//2+(c-b)
else:
    ans = (b-a)//2+(c-b)+2
print(ans)
