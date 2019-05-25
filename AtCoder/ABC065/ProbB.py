n = int(input())
a = [0] + [int(input()) for _ in range(n)]

visited = [0]*(n+1)
visited[1] = 1
cur = 1
ans = 0
while True:
    cur = a[cur]
    ans += 1
    visited[cur] += 1
    if visited[cur] > 1:
        print(-1)
        break
    elif cur == 2:
        print(ans)
        break

