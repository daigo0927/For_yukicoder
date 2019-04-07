a, b = map(int, input().split())

def count_bin(n, d):
    if n < 0:
        return 0
    div = (n+1)//2**(d+1)
    res = div*(2**d)
    remain = (n+1) - div*(2**(d+1))
    res += remain - 2**d if remain > 2**d else 0
    return res

ans = 0
for d in range(50):
    n_bin = count_bin(b, d) - count_bin(a-1, d)
    if n_bin%2 > 0:
        ans += 2**d
print(ans)
