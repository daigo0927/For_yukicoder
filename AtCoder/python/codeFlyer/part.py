a = int(input())
b = int(input())
for i in range(a):
    if (a-i)%b == 0:
        print(a-i)
        break;
