n, k = map(int, input().split())
a = list(map(int, input().split()))

ans = 0
for d in range(40, -1, -1):
    x = 1<<d
    n_bin = len([1 for i in range(n) if a[i]&x > 0])
    if n_bin < n-n_bin and x <= k: # less bit:1 than bit:0 in d-th digit in a -> put bit:1 in the answer
        n_bin = n - n_bin # number of 0-bit, added to the answer via xor
        k -= x # subtract d-th bit from k
    ans += x*n_bin

print(ans)
