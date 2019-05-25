import math
n = int(input())
a = list(map(int, input().split()))

class BIT:
    def __init__(self, n):
        self.n = n
        self.bit = [0]*(n+1)

    def sum(self, i):
        s = 0
        while i > 0:
            s += self.bit[i]
            i -= i&(-i)
        return s

    def add(self, i, x):
        while i <= self.n:
            self.bit[i] += x
            i += i&(-i)
            
a_sorted = sorted(list(set(a)))
left, right = 0, len(a_sorted) # number of unique elements of a
while right-left > 1: # bisection search: O(logA)
    mid = (left+right)//2 # target index
    num = 0 # number of ranges with majority >= a_sorted[mid]
    bit = BIT(2*n+1) # create BIT, size:2*n+1 is because cumulative-sum can be negative value
    cumsum = 0 # cumulative sum
    bit.add(cumsum+n, 1)
    for i in range(n): # O(n)
        print(bit.bit)
        cumsum += 1 if a[i] >= a_sorted[mid] else -1 # update region sum by comparison
        num += bit.sum(cumsum+n) # add #ranges by cumsum+n: O(logn)
        bit.add(cumsum+n, 1) # increment BIT element at cumsum+n(=count of interested regions)
    print(bit.bit, left, right)

    # update search range
    if num >= math.ceil(n*(n+1)//4):
        left = mid
    else:
        right = mid
print(a_sorted[left])
