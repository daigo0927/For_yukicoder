a, b, c = list(map(int , input().split()))
k = int(input())

if a == max(a, b, c):
    ans = a*2**k + b + c
elif b == max(a, b, c):
    ans = a + b*2**k + c
else:
    ans = a + b + c*2**k
print(ans)
