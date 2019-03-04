a, b, q = map(int, input().split())
s = [int(input()) for _ in range(a)]
t = [int(input()) for _ in range(b)]
x = [(int(input()), i) for i in range(q)]
x = sorted(x)

def check(x, s0, s1, t0, t1):
    ans = float('inf')
    for x1, x2 in [(s0, t0), (s0, t1), (s1, t0), (s1, t1),
                   (t0, s0), (t0, s1), (t1, s0), (t1, s1)]:
        ans = min(ans, abs(x-x1)+abs(x1-x2))
    return ans

s0, t0 = -float('inf'), -float('inf')
s1, t1 = s[0], t[0]
i_s, i_t = 0, 0
answers = []
for x_i, i in x:
    while s1 < x_i and i_s < a-1:
        s0 = s1
        i_s += 1
        s1 = s[i_s]
    while t1 < x_i and i_t < b-1:
        t0 = t1
        i_t += 1
        t1 = t[i_t]
    ans = check(x_i, s0, s1, t0, t1)
    answers.append((i, ans))

for _, ans in sorted(answers):
    print(ans)
