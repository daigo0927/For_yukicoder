n = int(input())

m = 0
i = 1
while True:
    m += i
    if m == n:
        print('Yes')
        print(i+1)
        break
    elif m > n:
        print('No')
        exit()
    i += 1

ans = [[1], [1]]
max_ = 0
if i == 1:
    print('1 1')
    print('1 1')
else:
    max_a = 1
    for i_ in range(1, i):
        adds = list(range(max_a+1, max_a+1+len(ans)))
        for j, add in enumerate(adds):
            ans[j].append(add)
        ans.append(adds)
        max_a = adds[-1]
    for a in ans:
        print(str(len(a))+' '+' '.join(map(str, a)))
