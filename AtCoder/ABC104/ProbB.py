s = input()

if s[0] == 'A':
    count = 0
    idx = -1
    for i, ss in enumerate(s[2:-1]):
        if ss == 'C':
            idx = i+2
            count += 1
    if count == 1:
        is_small = True
        for ss in s[1:idx]+s[idx+1:]:
            if ord(ss) < 97:
                is_small = False
                break
        if is_small:
            print('AC')
        else:
            print('WA')
        
    else:
        print('WA')
        
else:
    print('WA')
        
    
