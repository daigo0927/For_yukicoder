ab = input()

ab = int(ab.replace(' ', ''))
if int(ab**(1/2))**2 == ab:
    print('Yes')
else:
    print('No')
