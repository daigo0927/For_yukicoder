from collections import deque

n, m = list(map(int, input().split()))
paths = {}
for i in range(m):
    l, r, d = list(map(int, input().split()))
    if not l in paths.keys():
        paths[l] = [(r, d)]
    else:
        paths[l].append((r, d))
    if not r in paths.keys():
        paths[r] = [(l, -d)]
    else:
        paths[r].append((l, -d))
      
x = [None]*(n+1)
for i in range(1, n+1):
    if x[i] is None:
        x[i] = 0
        que = deque([i])
        while len(que) > 0:
            j = que.popleft()
            if not j in paths.keys():
                continue
            for k, d in paths[j]:
                if x[k] is None:
                    x[k] = x[j] + d
                    que.append(k)
                elif x[k] != x[j] + d:
                    print('No')
                    exit()
# print(x)
print('Yes')
        
