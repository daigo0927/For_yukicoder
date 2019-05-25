n = int(input())
t = list(map(int, input().split()))
v = list(map(int, input().split()))

t_cumsum = [t[0]]
for i in range(1, n):
    t_cumsum.append(t[i]+t_cumsum[i-1])

v_max = [0]    
idx = 0
for i in range(1, 2*sum(t)+1):
    time = i/2
    if time < t_cumsum[idx]:
        v_max.append(v[idx])
    elif time == t_cumsum[-1]:
        v_max.append(0)
    else:
        v_max.append(min(v[idx], v[idx+1]))
        idx += 1
# print(len(v_max), v_max)
    
vs = [0]*len(v_max)
for i in range(1, len(v_max)):
    vs[i] = min(vs[i-1]+0.5, v_max[i])
for i in range(len(v_max)-2, -1, -1):
    vs[i] = min(vs[i], vs[i+1]+0.5, v_max[i])
# print(vs)

ans = 0
for v0, v1 in zip(vs[:-1], vs[1:]):
    ans += (v0+v1)/2*0.5
print(ans)
