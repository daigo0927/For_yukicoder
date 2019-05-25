import math

def solve():
    n, a, b = list(map(int, input().split()))
    h = [int(input()) for _ in range(n)]
    h = sorted(h)

    def is_enough(t):
        t_check = 0
        for hh in h:
            hh -= b*t
            if hh > 0:
                t_check += math.ceil(hh/(a-b))
        if t_check > t: return False
        else: return True

    t_min = 1
    t_max = h[-1]//b+1 # number of spell
    while t_min != t_max-1:
        t_next = (t_min+t_max)//2
        if is_enough(t_next):
            t_max = t_next
        else:
            t_min = t_next
        # print(t_min, t_max)

    if is_enough(t_min): print(t_min)
    else: print(t_max)
    return

solve()
