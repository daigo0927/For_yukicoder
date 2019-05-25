sa = input()
sb = input()
sc = input()

s = sa[0]
sa = sa[1:]
while(True):
    if s == 'a':
        if len(sa) == 0:
            print('A')
            break
        else:
            s = sa[0]
            sa = sa[1:]
    elif s == 'b':
        if len(sb) == 0:
            print('B')
            break
        else:
            s = sb[0]
            sb = sb[1:]
    else:
        if len(sc) == 0:
             print('C')
             break
        else:
            s = sc[0]
            sc = sc[1:]

        
