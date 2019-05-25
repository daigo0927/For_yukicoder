from math import floor, ceil
a, b, x = list(map(int, input().split()))

if a == 0 and b == 0:
    print(1)
elif a%x == 0 and b%x == 0:
    print((b-a)//x+1)
elif a%x == 0:
    b_ = (b//x)*x
    print((b_-a)//x+1)
elif b%x == 0:
    a_ = ((a//x)+1)*x
    print((b-a_)//x+1)
else:
    a_ = ((a//x)+1)*x
    b_ = (b//x)*x
    print((b_-a_)//x+1)
