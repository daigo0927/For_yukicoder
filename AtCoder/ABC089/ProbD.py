h, w, d = list(map(int, input().split()))
a = [list(map(int, input().split())) for _ in range(h)]
q = int(input())
lr = [list(map(int, input().split())) for _ in range(q)]

a_and_pos = {}
for i in range(h):
    for j in range(w):
        a_and_pos[a[i][j]] = (i, j)

costs = [0]*(h*w+1)
for x in range(d+1, h*w+1):
    i_prev, j_prev = a_and_pos[x-d]
    i, j = a_and_pos[x]
    costs[x] = costs[x-d] + abs(i-i_prev) + abs(j-j_prev)
# print(costs)

for l, r in lr:
    print(costs[r] - costs[l])
