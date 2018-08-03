n, W = list(map(int, input().split()))
wv = [list(map(int, input().split())) for _ in range(n)]

w0 = wv[0][0]
wv_dict = {w0:[], w0+1:[], w0+2:[], w0+3:[]}
for w, v in wv:
    wv_dict[w].append(v)
for w, vs in wv_dict.items():
    vs = sorted(vs)[::-1]
    wv_dict[w] = [0]
    for v in vs:
        wv_dict[w].append(v + wv_dict[w][-1])
# print(wv_dict)

ans = 0
for i in range(len(wv_dict[w0])):
    for j in range(len(wv_dict[w0+1])):
        for k in range(len(wv_dict[w0+2])):
            for l in range(len(wv_dict[w0+3])):
                w_sum = i*w0 + j*(w0+1) + k*(w0+2) + l*(w0+3)
                if w_sum > W: continue

                ans = max(ans, wv_dict[w0][i]+wv_dict[w0+1][j]+wv_dict[w0+2][k]+wv_dict[w0+3][l])
print(ans)
