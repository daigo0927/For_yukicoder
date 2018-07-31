from copy import deepcopy
from math import factorial as fact
def combi(n, r):
    return fact(n)//(fact(n-r)*fact(r))

n, a, b = list(map(int, input().split()))
v = list(map(int, input().split()))
v_num = {}
for i in range(n):
    if v[i] not in v_num.keys():
        v_num[v[i]] = 1
    else:
        v_num[v[i]] += 1

v = sorted(v)
ans1 = v[-a:]
print(sum(ans1)/a)

answers = [ans1]
for i in range(a+1, b+1):
    if sum(v[-i:])/i == sum(ans1)/a:
        answers.append(v[-i:])
    else:
        break
# print(answers)

ans2 = 0
for ans in answers:
    ans_num = {}
    for i in range(len(ans)):
        if ans[i] not in ans_num.keys():
            ans_num[ans[i]] = 1
        else:
            ans_num[ans[i]] += 1
        
    a2 = 1
    for k in ans_num.keys():
        a2 *= combi(v_num[k], ans_num[k])
    ans2 += a2
    
print(ans2)
