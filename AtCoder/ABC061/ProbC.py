n, k = list(map(int, input().split()))
n_map = {}
for _ in range(n):
    a, b = list(map(int, input().split()))
    if not a in n_map.keys():
        n_map[a] = b
    else:
        n_map[a] += b

num = 0
for n in sorted(n_map.keys()):
    num += n_map[n]
    if num >= k:
        print(n)
        break

