MOD = 10**9+7

n = int(input())

def get_primes(n_max):
    count = 0
    ps = [2, 3]

    for n in range(5, n_max+1, 2):
        is_p = True
        for i in range(1, len(ps)):
            count += 1
            if ps[i]**2 > n:
                break
            count += 1
            if n%ps[i] == 0:
                is_p = False
                break
        if is_p:
            ps.append(n)
    return ps
            
primes = get_primes(n)
p_dict = dict(zip(primes, [0]*len(primes)))
ns = [i for i in range(n+1)]
for i in range(2, n+1):
    p = ns[i]
    if p == 1: continue
    p_dict[p] += n//i
    for j in range(i, n+1, i):
        ns[j] = ns[j]//p

# print(p_dict)
ans = 1
for key, item in p_dict.items():
    ans = ans*(item+1)%MOD
print(ans)
