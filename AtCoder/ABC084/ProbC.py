import math

n = int(input())
c, s, f = [], [], []
for i in range(n-1):
    c_, s_, f_ = list(map(int, input().split()))
    c.append(c_)
    s.append(s_)
    f.append(f_)

for i in range(n-1):
    t = s[i]
    t += c[i]
    for j in range(i+1, n-1):
        if t < s[j]:
            t = s[j]
        else:
            t = f[j]*math.ceil(t/f[j])
        t += c[j]
    print(t)
print(0)
