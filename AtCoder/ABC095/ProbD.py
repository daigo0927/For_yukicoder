from itertools import accumulate
n, c = list(map(int, input().split()))
xv = [list(map(int, input().split())) for _ in range(n)]

v_cum = [0]*(n+1)
for i in range(n):
    v_cum[i+1] = v_cum[i] + xv[i][1]

for_cal = [0] + [v_cum[i+1] - xv[i][0] for i in range(n)]
fb_cal = [0] + [v_cum[i+1] - 2*xv[i][0] for i in range(n)]

for_cum = [x for x in accumulate(for_cal, max)]
fb_cum = [x for x in accumulate(fb_cal, max)]

ans = 0
for i in range(n+1):
    # OA path
    j = n if i == 0 else i-1

    # OB path
    ob_x = 0 if i == 0 else c - xv[i-1][0]
    ob_v = v_cum[n] - v_cum[i-1]

    # for-back root
    ans = max(ans, fb_cum[j]+ob_v-ob_x)
    # back-for path
    ans = max(ans, for_cum[j]+ob_v-2*ob_x)

print(ans)
