n = int(input())

invalid = True
while n > 0:
    if n%7 == 0 or n%4 == 0:
        print('Yes')
        invalid = False
        break
    else:
        n -= 4
        
if invalid:
    print('No')
