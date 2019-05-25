n, k = list(map(int, input().split()))

if k == 1:
    print(n**3)
elif k == 2:
    odd = (n+1)//2
    even = n//2
    print(odd**3+even**3)
else:
    m = n//k
    if k%2 == 0:
        half = n//(k//2)-m
    else:
        half = 0
    print(m**3+half**3)
