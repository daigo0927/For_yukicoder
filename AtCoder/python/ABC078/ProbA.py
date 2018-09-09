x, y = input().split()

x, y = int(x, 16), int(y, 16)
if x < y:
    print('<')
elif x > y:
    print('>')
else:
    print('=')
