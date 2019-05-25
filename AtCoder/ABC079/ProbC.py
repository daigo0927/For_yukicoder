a, b, c, d = list(map(int, list(input())))

ops = {'+', '-'}

for op1 in ops:
    if op1 == '+': ab = a+b
    else: ab = a-b
    
    for op2 in ops:
        if op2 == '+': abc = ab+c
        else: abc = ab-c
        
        for op3 in ops:
            if op3 == '+': abcd = abc+d
            else: abcd = abc-d

            if abcd == 7:
                a, b, c, d = map(str, [a, b, c, d])
                print(a+op1+b+op2+c+op3+d+'=7')
                exit()
