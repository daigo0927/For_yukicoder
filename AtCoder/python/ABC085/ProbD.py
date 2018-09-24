import math

n, h = list(map(int, input().split()))
a, b = [], []
for _ in range(n):
    a_i, b_i = list(map(int, input().split()))
    a.append([a_i, 'a'])
    b.append([b_i, 'b'])
damages = sorted(a+b, reverse = True)

ans = 0
for d, is_ab in damages:
    if is_ab == 'a':
        ans += math.ceil(h/d)
        break
    else:
        h -= d
        ans += 1
        if h <= 0:
            break

print(ans)
