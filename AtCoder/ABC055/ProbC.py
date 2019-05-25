n, m = list(map(int, input().split()))

if m < 2:
    print(0)
else:
    if m <= 2*n:
        print(m//2)
    else:
        ans = n
        m -= 2*n
        ans += m//4
        print(ans)
