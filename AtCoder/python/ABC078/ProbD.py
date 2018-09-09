n, z, w = list(map(int, input().split()))
a = list(map(int, input().split()))

if n == 1:
    print(abs(a[0]-w))
else:
    ans1 = abs(a[-1] - w)
    ans2 = abs(a[-2] - a[-1])
    print(max(ans1, ans2))
