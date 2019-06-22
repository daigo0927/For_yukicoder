n = int(input())
w = list(map(int, input().split()))

s1, s2 = 0, sum(w)
ans = abs(s2 - s1)
for i in range(n):
    s1 += w[i]
    s2 -= w[i]
    ans = min(ans, abs(s2 - s1))
print(ans)
    
