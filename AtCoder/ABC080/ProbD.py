T_MAX = 10**5
n, nc = list(map(int, input().split()))
stc = [list(map(int, input().split())) for _ in range(n)]

recs = [[0]*(T_MAX+1) for c in range(nc+1)]
for s, t, c in stc:
    recs[c][s-1:t] = [1]*(t-s+1)

ans = max(map(sum, zip(*recs)))
print(ans)
