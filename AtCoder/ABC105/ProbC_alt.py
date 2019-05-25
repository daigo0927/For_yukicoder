n = int(input())

def solve(n):
    if n == 0:
        print(0)
        return
    ans = ''
    while n != 0:
        if n%2 == 1:
            ans = '1'+ans
            n = int((n-1)/(-2))
        else:
            ans  = '0'+ans
            n = int(n/(-2))
    print(ans)
    return
        
solve(n)
