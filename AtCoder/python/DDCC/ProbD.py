a = [int(input()) for _ in range(29)]

def gcd(x, y):
    if y > 0:
        d, y_new, x_new = gcd(y, x%y)
        y_new -= (x//y)*x_new
        return d, x_new, y_new
    else:
        return x, 1, 0

def check(x, n):
    s = 0
    while x:
        s += x%n
        x //= n
    return s

remains = [(aa%(i-1), i-1) for i, aa in enumerate(a, 2)]
ans, d = 0, 1
for b, n in remains:
    g, n1, n2 = gcd(d, n)
    ans, d = (n*n2*ans + d*n1*b)//g, d*(n//g)
    ans %= d

valid = True
if ans > 10**12:
    valid = False
for i, aa in enumerate(a, 2):
    if check(ans, i) != aa:
        valid = False
if valid:
    print(ans)
else:
    print('invalid')
