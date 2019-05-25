n = int(input())
a = list(map(int, input().split()))
b = list(map(int, input().split()))
c = list(map(int, input().split()))

a = sorted(a)[::-1]
b = sorted(b)[::-1]
c = sorted(c)[::-1]

a_smaller_b = [0]*n
b_smaller_c = [0]*n
n_a, n_b = 0, 0
j, k = 0, 0
for i in range(n):
    a_tar = a[i]
    b_tar = b[i]
    while True:
        if j == n:
            a_smaller_b[i] = n_a
            break
        if b[j] > a_tar:
            n_a += 1
            j += 1
        else:
            a_smaller_b[i] = n_a
            break

    while True:
        if k == n:
            b_smaller_c[i] = n_b
            break
        if c[k] > b_tar:
            n_b += 1
            k += 1
        else:
            b_smaller_c[i] = n_b
            break
# print(a_smaller_b)
# print(b_smaller_c)

bsc_cumsum = [0]*(n+1)
for i in range(n):
    bsc_cumsum[i+1] = bsc_cumsum[i]+b_smaller_c[i]

ans = 0
for i in range(n):
    ans += bsc_cumsum[a_smaller_b[i]]
print(ans)
