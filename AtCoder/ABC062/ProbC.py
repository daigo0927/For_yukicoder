def solve(h, w):
    w1 = round(w/3)
    s1 = h*w1
    w21 = w - w1
    h2 = h//2
    s21 = h2*w21
    h3 = h - h2
    s31 = h3*w21
    ans1 = max([s1, s21, s31]) - min([s1, s21, s31])

    w22 = w21//2
    s22 = h*w22
    w32 = w - w1 - w22
    s32 = h*w32
    ans2 = max([s1, s22, s32]) - min([s1, s22, s32])

    return min(ans1, ans2)

h, w = list(map(int, input().split()))

if h%3 == 0 or w%3 == 0:
    print(0)
else:
    ans1 = solve(h, w)
    ans2 = solve(w, h)
    print(min([ans1, ans2]))
