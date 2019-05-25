n = int(input())
a = list(map(int, input().split()))

cumsum = [a[0]]
for i in range(1, n):
    cumsum.append(cumsum[i-1]+a[i])

i, k = 0, 2
ans = 10**18
for j in range(1, n-2):
    while True:
        p = cumsum[i]
        q = cumsum[j] - cumsum[i]
        p_new = cumsum[i+1]
        q_new = cumsum[j] - cumsum[i+1]
        if abs(p_new-q_new) < abs(p-q):
            i += 1
        else:
            break

    while True:
        r = cumsum[k] - cumsum[j]
        s = cumsum[-1] - cumsum[k]
        r_new = cumsum[k+1] - cumsum[j]
        s_new = cumsum[-1] - cumsum[k+1]
        if abs(r_new-s_new) < abs(r-s):
            k += 1
        else:
            break

    ans = min(ans, max([p, q, r, s]) - min([p, q, r, s]))
    # print(ans, ':', i, j, k, ':', p, q, r, s)
print(ans)
