n, l = list(map(int, input().split()))
s = [input().strip() for i in range(n)]
# print(s)

ans = ''
for ss in sorted(s):
    ans += ss
print(ans)
