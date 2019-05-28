n = int(input())

sp = {}
for i in range(n):
    s, p = input().split()
    p = int(p)
    if s not in sp.keys():
        sp[s] = [(p, i+1)]
    else:
        sp[s].append((p, i+1))

ss = sorted(list(set(sp.keys())))
for s in ss:
    for p, i in sorted(sp[s], reverse = True):
        print(i)
       
