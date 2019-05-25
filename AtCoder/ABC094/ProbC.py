n = int(input())
x = list(map(int, input().split()))

x_sorted = sorted(x)
meds = x_sorted[n//2-1:n//2+1]
for i in range(n):
    if x[i] <= meds[0]:
        print(meds[1])
    elif x[i] >= meds[1]:
        print(meds[0])
