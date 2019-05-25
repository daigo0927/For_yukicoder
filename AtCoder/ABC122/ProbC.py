n, q = map(int, input().split())
s = input()

n_ac = [0]*(n+1)
for i in range(1, n):
    if s[i-1] == 'A' and s[i] == 'C':
        n_ac[i+1] = n_ac[i] + 1
    else:
        n_ac[i+1] = n_ac[i]
# print(n_ac)
        
for _ in range(q):
    l, r = map(int, input().split())
    print(n_ac[r] - n_ac[l])
    



