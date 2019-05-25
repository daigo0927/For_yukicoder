from collections import deque

n, k, l = list(map(int, input().split()))

def get_groups(n, m):
    road = [[] for _ in range(n+1)]
    for _ in range(m):
        p, q = list(map(int, input().split()))
        road[p].append(q)
        road[q].append(p)

    groups = [0]*(n+1)
    group_idx = 1
    connect = deque()
    for i in range(1, n+1):
        if groups[i] == 0:
            groups[i] = group_idx
            connect.clear()
            connect.append(i)
            while len(connect) > 0:
                cnct = connect.popleft()
                for c in road[cnct]:
                    if groups[c] == 0:
                        groups[c] = group_idx
                        connect.append(c)
            group_idx += 1
            
    return groups

road_groups = get_groups(n, k)
train_groups = get_groups(n, l)
# print(road_groups, train_groups)
pairs = {}
for c in range(1, n+1):
    key = (road_groups[c], train_groups[c])
    if not key in pairs.keys():
        pairs[key] = 1
    else:
        pairs[key] += 1

ans = []
for c in range(1, n+1):
    key = (road_groups[c], train_groups[c])
    ans.append(str(pairs[key]))
print(' '.join(ans))
