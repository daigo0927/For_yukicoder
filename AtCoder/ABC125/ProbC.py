n = int(input())
a = list(map(int, input().split()))

def gcd(x, y):
    x, y = max(x, y), min(x, y)
    while x%y > 0:
        x, y = y, x%y
    return y

a = sorted(a)
ans = [gcd(a[0], a[1]), a[0]]
for i in range(2, n):
    ans_0, ans_1 = ans
    ans_0_new = gcd(ans_0, a[i])
    ans_1_new = max(ans_0, gcd(ans_1, a[i]))
    ans = [ans_0_new, ans_1_new]
ans_2 = a[1]
for i in range(2, n):
    ans_2 = gcd(ans_2, a[i])
print(max(ans+[ans_2]))
