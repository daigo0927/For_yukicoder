def solve():
    n = int(input())
    s = [int(input()) for _ in range(n)]
    s = sorted(s)

    if sum(s)%10 != 0:
        print(sum(s))
        return
    else:
        for ss in s:
            if ss%10 != 0:
                print(sum(s)-ss)
                return
        print(0)

solve()
