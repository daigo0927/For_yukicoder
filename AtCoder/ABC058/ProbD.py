MOD = int(10**9+7)
n, m = list(map(int, input().split()))
x = list(map(int, input().split()))
y = list(map(int, input().split()))

x_mul = 0
y_mul = 0
for i in range(n):
    x_mul += (i-(n-i-1))*x[i]%MOD
for i in range(m):
    y_mul += (i-(m-i-1))*y[i]%MOD
print(x_mul*y_mul%MOD)
