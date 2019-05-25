NMAX = 10**5+1

is_prime = [True]*NMAX
for i in range(2, NMAX):
    if is_prime[i]:
        for j in range(2*i, NMAX, i):
            is_prime[j] = False

sim_2017 = [0]*NMAX
for i in range(3, NMAX, 2):
    if is_prime[i] and is_prime[(i+1)//2]:
        sim_2017[i] += 1
for i in range(1, NMAX):
    sim_2017[i] += sim_2017[i-1]

q = int(input())
for _ in range(q):
    l, r = list(map(int, input().split()))
    ans = sim_2017[r] - sim_2017[l-1]
    print(ans)
