n = int(input())
t, a = map(int, input().split())
h = list(map(int, input().split()))

ans = 0
diff = 10**9
for i in range(n):
    if abs(a - (t-h[i]*0.006)) < diff:
        ans = i+1
        diff = abs(a - (t-h[i]*0.006))
print(ans)
