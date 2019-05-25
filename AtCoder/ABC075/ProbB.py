h, w = list(map(int, input().split()))
s = [input() for _ in range(h)]
s_large = [''.join(['.']*(w+2))]\
          + ['.'+s[i]+'.' for i in range(h)]\
          + [''.join(['.']*(w+2))]
# for i in range(len(s)):
#     print(s[i])

for i in range(h):
    for j in range(w):
        n = 0
        if s[i][j] == '#':
            continue
        for ii in [i, i+1, i+2]:
            for jj in [j, j+1, j+2]:
                if s_large[ii][jj] == '#':
                    n += 1
        s[i] = s[i][:j]+str(n)+s[i][j+1:]

for i in range(h):
    print(s[i])
