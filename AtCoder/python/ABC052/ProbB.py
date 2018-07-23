n = int(input())
s = input()

x_max = 0
x = 0
for i in range(n):
    if s[i] == 'I':
        x += 1
    else:
        x -= 1

    if x > x_max:
        x_max = x
print(x_max)
