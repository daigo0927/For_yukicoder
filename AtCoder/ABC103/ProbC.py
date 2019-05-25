n = int(input())
a = list(map(int, input().split()))

def lcm(x_, y_):
    x, y = max(x_, y_), min(x_, y_)
    while x%y > 0:
        x, y = y, x%y
    gcd = y
    return x_*y_//gcd

a_lcm = a[0]
for i in range(1, n):
    a_lcm = lcm(a_lcm, a[i])
ans = 0
for i in range(n):
    ans += (a_lcm-1)%a[i]
print(ans)
