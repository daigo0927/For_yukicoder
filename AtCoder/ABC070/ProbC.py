n = int(input())
t = [int(input()) for _ in range(n)]

def scm(a, b):
    x, y = max(a, b), min(a, b)
    while x%y > 0:
        tmp = x%y
        x = y
        y = tmp
    return a*b//y

scm_ = t[0]
for i in range(1, n):
    scm_ = scm(scm_, t[i])
print(scm_)
