n = int(input())
a = list(map(int, input().split()))
mean1 = int(sum(a)/n)
mean2 = mean1+1
ans1 = 0
ans2 = 0
for aa in a:
    ans1 += (aa-mean1)**2
    ans2 += (aa-mean2)**2
print(min(ans1, ans2))
