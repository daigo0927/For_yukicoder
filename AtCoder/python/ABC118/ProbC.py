n = int(input())
a = list(map(int, input().split()))

def gcm(x, y):
    x, y = max(x, y), min(x, y)
    while x%y > 0:
        x, y = y, x%y
    return y

a_gcd = a[0]
for i in range(n):
    a_gcd = gcm(a_gcd, a[i])
print(a_gcd)
