H, W = list(map(int, input().split(' ')))
N, M = list(map(int, input().split(' ')))
hanko = [input() for _ in range(N)]

H_ = min(N*2+1, H)
W_ = min(M*2+1, W)

paper = [[0]*(W_+1) for _ in range(H_+1)]
for y in range(N):
    for x in range(M):
        if hanko[y][x] == '#':
            y_end = H_-N+y+1
            x_end = W_-M+x+1
            paper[y][x] += 1
            paper[y_end][x] -= 1
            paper[y][x_end] -= 1
            paper[y_end][x_end] += 1
paper = [paper[h][:-1] for h in range(H_)]


for h in range(H_):
    p = paper[h]
    for w in range(1, W_):
        p[w] += p[w-1]

for h in range(1, H_):
    p = paper[h-1]
    pp = paper[h]
    for w in range(W_):
        pp[w] += p[w]

num_black = 0
if H <= N*2+1 and W <= M*2+1:
    for h in range(H_):
        p = paper[h]
        for w in range(W_):
            num_black += (p[w]>0)

elif H > N*2+1 and W <= M*2+1:
    for h in range(H_):
        p = paper[h]
        for w in range(W_):
            r = 1
            if h == N:
                r *= (H - N*2)
            num_black += (p[w]>0)*r
    
elif H <= N*2+1 and W > M*2+1:
    for h in range(H_):
        p = paper[h]
        for w in range(W_):
            r = 1
            if w == M:
                r *= (W - M*2)
            num_black += (p[w]>0)*r

elif H > N*2+1 and W > M*2+1:
    for h in range(H_):
        p = paper[h]
        for w in range(W_):
            r = 1
            if h == N:
                r *= (H - N*2)
            if w == M:
                r *= (W - M*2)
            num_black += (p[w]>0)*r

print(num_black)
