n = int(input())
a = list(map(int, input().split()))

from itertools import accumulate
accum = list(accumulate(a))

i_left = 0
i_right = 2
ans = 10**18
for i in range(1, n-2):
    while True:
        p = accum[i_left]
        q = accum[i] - p
        p_new = accum[i_left+1]
        q_new = accum[i] - p_new
        if abs(p_new - q_new) < abs(p - q):
            i_left += 1
        else:
            break
    while True:
        r = accum[i_right] - accum[i]
        s = accum[-1] - accum[i_right]
        r_new = accum[i_right+1] - accum[i]
        s_new = accum[-1] - accum[i_right+1]
        if abs(r_new - s_new) < abs(r - s):
            i_right += 1
        else:
            break

    # print(p, q, r, s)
    diff = max([p, q, r, s]) - min([p, q, r, s])
    ans = min(ans, diff)

print(ans)
