n = int(input())
if n == 0:
    print(0)
else:
    d = 0
    pows = [(0, 1)]
    for i in range(1, 50):
        a, b = pows[i-1]
        if i%2 == 1:
            min_ = b-2**(i+1)+1
            pows.append((min_, min_+2**i-1))
        else:
            max_ = a+2**(i+1)-1
            pows.append((max_-2**i+1, max_))
    pows[0] = (1, 1)
    # for p in pows: print(p)

    ans = ''
    d = len(pows)-1
    for p in pows[::-1]:
        pmin, pmax = p
        if n >= pmin and n <= pmax:
            ans += '1'
            n -= (-2)**d
            # print((-2)**d)
        else:
            ans += '0'

        d -= 1
    print(ans.lstrip('0'))



        

    
