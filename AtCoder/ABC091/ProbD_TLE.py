""" !!!This solution is collect but get TLE in python!!! """
n = int(input())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

ans = 0
for k in range(28, -1, -1):
    i_1, i_2, i_3 = 0, 0, 0
    T = 1<<k
    add = 0

    for i in range(n):
        a[i] %= 2*T
        b[i] %= 2*T

    a = sorted(a, reverse = True)
    b = sorted(b)
    for i in range(n):
        while i_1 < n and a[i]+b[i_1] < T:
            i_1 += 1
        while i_2 < n and a[i]+b[i_2] < 2*T:
            i_2 += 1
        while i_3 < n and a[i]+b[i_3] < 3*T:
            i_3 += 1
        add += (i_2-i_1) + (n-i_3)

    if add%2 == 1:
        ans += T

print(ans)
