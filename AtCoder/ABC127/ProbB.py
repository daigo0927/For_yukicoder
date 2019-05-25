r, D, x_2000 = map(int, input().split())

x = x_2000
for i in range(1, 11):
    x = r*x - D
    print(x)
