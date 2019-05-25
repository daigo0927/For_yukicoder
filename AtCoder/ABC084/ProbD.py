import math
RMAX = 10**5

def get_primes(n):
    ps = []
    upper = math.sqrt(n)
    data = [i+1 for i in range(1, n)]
    while True:
        p = data[0]
        if p >= upper:
            break
        ps.append(p)
        data = [e for e in data if e%p != 0]
    return ps + data

primes = get_primes(RMAX)
primes_set = set(primes)
sim_2017 = [0]*(RMAX+1)
for p in primes:
    if (p+1)//2 in primes_set:
        sim_2017[p] = 1

for i in range(1, len(sim_2017)):
    sim_2017[i] += sim_2017[i-1]

q = int(input())
for _ in range(q):
    l, r = list(map(int, input().split()))
    ans = sim_2017[r] - sim_2017[l-1]
    print(ans)
