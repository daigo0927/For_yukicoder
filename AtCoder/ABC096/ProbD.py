n = int(input())

primes = []
nums = list(range(2, 55556))
while True:
    p = nums[0]
    if p > int(55556**(1/2)):
        primes += nums
        break
    primes.append(p)
    nums = [num for num in nums if num%p > 0]
# print(primes[:20])

ans = [p for p in primes if str(p)[-1] == '1']
print(' '.join(list(map(str, ans[:n]))))
