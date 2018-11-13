n, k = map(int, input().split())
a = list(map(int, input().split()))

for i in range(n):
    if a[i] == 1:
        min_idx = i
        break
ans = 10**9
for i in range(k):
    ans_cur = 1
    l = min_idx - i
    r = l + (k-1)
    if l > 0:
        ans_cur += l//(k-1)+1 if l%(k-1) > 0 else l//(k-1)
    if r < n-1:
        ans_cur += (n-1-r)//(k-1)+1 if (n-1-r)%(k-1) > 0 else (n-1-r)//(k-1)
    ans = min(ans, ans_cur)
print(ans)
