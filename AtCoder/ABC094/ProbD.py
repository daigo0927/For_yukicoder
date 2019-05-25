n = int(input())
a = list(map(int, input().split()))

a = sorted(a)
ai = a[-1]
aj = -1
for j in range(n-1):
    if abs(ai/2-a[j]) < abs(ai/2-aj):
        aj = a[j]
print(ai, aj)
