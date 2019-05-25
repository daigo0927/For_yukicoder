import math # in python3.4.3 math -> fractions
n, X = list(map(int, input().split()))
x = list(map(int, input().split()))

x = sorted(x+[X])
x_diff = [x[i+1]-x[i] for i in range(n)]
# print(x, x_diff)
ans = x_diff[0]
for i in range(1, n):
    ans = math.gcd(ans, x_diff[i])
print(ans)
