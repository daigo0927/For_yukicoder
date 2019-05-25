n = int(input())
a, b = map(int, input().split())
p = list(map(int, input().split()))

n1, n2, n3 = 0, 0, 0
for pp in p:
    if pp <= a:
        n1 += 1
    elif pp <= b:
        n2 += 1
    else:
        n3 += 1
print(min(n1, n2, n3))
