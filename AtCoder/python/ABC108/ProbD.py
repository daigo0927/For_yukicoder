l = int(input())

p = 0
while True:
    if 2**p > l:
        p -= 1
        break
    else:
        p += 1
        
n = p+1
m = 2*p
ans = []
for i in range(1, n):
    ans.append([i, i+1, 0])
    ans.append([i, i+1, 2**(i-1)])
    
while l > 2**p:
    for i in range(n-1, 0, -1):
        if l-2**(i-1) >= 2**p:
            ans.append([i, n, l-2**(i-1)])
            l = l-2**(i-1)
            m += 1
            break

print(n, m)
for a in ans:
    print(' '.join(list(map(str, a))))
