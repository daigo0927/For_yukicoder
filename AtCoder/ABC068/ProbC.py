n, m = list(map(int, input().split()))

connect_1 = {}
connect_n = {}
for i in range(m):
    a, b = list(map(int, input().split()))
    if a == 1:
        connect_1[b] = 1
    if b == n:
        connect_n[a] = 1
# print(connect_1.keys(), connect_n.keys())

ans = 'IMPOSSIBLE'
for k in connect_1.keys():
    if k in connect_n.keys():
        ans = 'POSSIBLE'
print(ans)
