from math import sqrt
n = int(input())

for i in range(1, int(sqrt(n))+1):
    if n%i == 0:
        a = i
        b = n//i
print(max(len(str(a)), len(str(b))))
