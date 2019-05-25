MOD = 10**9+7
n = int(input())
a = list(map(int, input().split()))
a = sorted(a)

if n%2 == 0:
    valid = True
    for i in range(n):
        if i%2 == 0: v = i+1
        else: v = i
        if a[i] != v:
            valid = False
            print(0)
            break
    if valid:
        print(2**(n//2)%MOD)

else:
    valid = True
    for i in range(n):
        if i%2 != 0: v = i+1
        else: v = i
        if a[i] != v:
            valid = False
            print(0)
            break
    if valid:
        print(2**(n//2)%MOD)


