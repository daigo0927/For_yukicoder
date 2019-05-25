s = input()
n = len(s)

ans0, ans1 = 0, 0
n0_even, n0_odd = 0, 0
for i in range(n):
    if s[i] == "0":
        if i%2 == 0:
            n0_even += 1
        else:
            n0_odd += 1
n1_even = (n+1)//2 - n0_even
n1_odd = n//2 - n0_odd
ans0 = n1_even+n0_odd
ans1 = n0_even+n1_odd
print(min(ans0, ans1))
