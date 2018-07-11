from math import sqrt

n = int(input())
s = int(input())

def f(b, n):
    if n < b:
        return n
    else:
        return f(b, n//b)+(n%b)

def solve(n, s):
    if s == n:
        print(n+1)
        return
    elif s > n:
        print(-1)
        return
    else:
        for i in range(2, int(sqrt(n))+1):
            if f(i, n) == s:
                print(i)
                return
            
        for i in range(int(sqrt(n)), 0, -1):
            b = (n-s)/i+1
            if b == int(b) and f(int(b), n) == s:
                print(int(b))
                return

        print(-1)
        return

solve(n, s)




        
