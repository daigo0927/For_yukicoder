a, b = list(map(int, input().split()))

L = 100
l = L//2
ans = [['.']*L for _ in range(l)]
ans += [['#']*L for _ in range(l)]
# for a in ans: print(a)

for i in range(a-1):
    h = (i//l)*2 + l+1
    w = (i%l)*2
    ans[h][w] = '.'
for i in range(b-1):
    h = (i//l)*2
    w = (i%l)*2
    ans[h][w] = '#'

print(L, L)
for a in ans:
    print(''.join(a))
