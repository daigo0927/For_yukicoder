n, m = list(map(int, input().split()))
a = list(map(int, input().split()))

cumsum = 0
remains = {0:1}
for i in range(n):
    cumsum += a[i]
    r = cumsum%m
    if not r in remains.keys():
        remains[r] = 1
    else:
        remains[r] += 1
# print(remains)

ans = 0
for k, v in remains.items():
    ans += v*(v-1)//2
print(ans)
