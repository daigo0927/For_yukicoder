import statistics
n = int(input())
a = list(map(int, input().split()))
a = [a[i]-(i+1) for i in range(n)]
# print(a)
med = statistics.median_low(a)
ans = 0
for i in range(len(a)):
    ans += abs(a[i] - med)
print(ans)
