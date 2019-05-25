import math
q = int(input())
ab = [list(map(int, input().split())) for _ in range(q)]

for a, b in ab:
    a, b = min(a, b), max(a, b)
    p = a*b
    n = math.ceil((-1+(1+4*p)**(1/2))/2)
    if a <= n:
        lower1 = a-1

    if b <= n:
        lower2 = b-1
    else:
        m = p//n if p%n > 0 else p//n-1
        n_lim = p//(a+1) if p%(a+1) > 0 else p//(a+1)-1
        if n > n_lim:
            lower2 = n_lim
        else:
            lower2 = n + m - (a+1)
            
    print(lower1+lower2)
