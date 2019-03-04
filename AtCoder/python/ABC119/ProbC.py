n, a, b, c = map(int, input().split())
l = [int(input()) for _ in range(n)]

ans = 10**9
for m in range(4**n):
    length = [0, 0, 0, 0]
    counts = [0, 0, 0, 0]
    for d in range(n-1, -1, -1):
        i = m//(4**d)
        length[i] += l[d]
        counts[i] += 1
        m %= 4**d
        
    if 0 in length[:3]:
        continue
    ans_tmp = 0
    for i in range(3):
        ans_tmp += abs([a,b,c][i] - length[i]) + 10*(counts[i]-1)
    ans = min(ans, ans_tmp)
print(ans)
