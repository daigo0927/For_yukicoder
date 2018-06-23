n = int(input())

n_str = str(n)
s = 0
for ns in n_str:
    s += int(ns)

# print(n, s)
if n%s == 0:
    print('Yes')
else:
    print('No')
    
