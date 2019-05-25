from collections import defaultdict
n = int(input())
if n in [1, 2]:
    print(0)
    exit()

count_primes = defaultdict(int, {})
for m in range(2, n+1):
    p = 2
    while p**2 <= m:
        while m%p == 0:
            m //= p
            count_primes[p] += 1
        p += 1
    if m > 1:
        count_primes[m] += 1
# print(count_primes)

count_div = [0]*100
for _, c in count_primes.items():
    for i in range(c+1):
        count_div[i] += 1
# print(count_div)

ans = count_div[74] + count_div[24]*(count_div[2]-1) \
    + count_div[14]*(count_div[4]-1) + count_div[4]*(count_div[4]-1)//2*(count_div[2]-2)
print(ans)
