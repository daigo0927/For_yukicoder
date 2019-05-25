n = int(input())
v = list(map(int, input().split()))

ans = 0
even = v[::2]
nums_e = {}
for e in even:
    if not e in nums_e.keys():
        nums_e[e] = 1
    else:
        nums_e[e] += 1

e_sorted = []
for key, value in nums_e.items():
    e_sorted.append([value, key])
e_sorted = sorted(e_sorted, reverse = True) + [[0, 0-1]]
        

odd = v[1::2]
nums_o = {}
for o in odd:
    if not o in nums_o.keys():
        nums_o[o] = 1
    else:
        nums_o[o] += 1
        
o_sorted = []
for key, value in nums_o.items():
    o_sorted.append([value, key])
o_sorted = sorted(o_sorted, reverse = True) + [[-1, 0]]

if e_sorted[0][1] != o_sorted[0][1]:
    print(n - e_sorted[0][0] - o_sorted[0][0])
else:
    ans1 = n - e_sorted[1][0] - o_sorted[0][0]
    ans2 = n - e_sorted[0][0] - o_sorted[1][0]
    print(min(ans1, ans2))
