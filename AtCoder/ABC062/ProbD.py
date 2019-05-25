import heapq
n = int(input())
a = list(map(int, input().split()))

a1 = a[:n]
heapq.heapify(a1)
a1_sum = sum(a1)
a1_sums = [a1_sum]
for i in range(n, 2*n):
    a1_min = heapq.heappop(a1) # pop the smallest value from a1
    if a[i] > a1_min:
        heapq.heappush(a1, a[i])
        a1_sum = a1_sum - a1_min + a[i]
    else:
        heapq.heappush(a1, a1_min)
    a1_sums.append(a1_sum)

a2 = a[-n:]
a2_sum = sum(a2)
a2_sums = [a2_sum]
a2_inv = [-aa for aa in a2]
heapq.heapify(a2_inv)
for i in range(2*n-1, n-1, -1):
    a2_max = -heapq.heappop(a2_inv) # pop the largest value from a2
    if a[i] < a2_max:
        heapq.heappush(a2_inv, -a[i])
        a2_sum = a2_sum - a2_max + a[i]
    else:
        heapq.heappush(a2_inv, -a2_max)
    a2_sums.append(a2_sum)
a2_sums = a2_sums[::-1] # reverse order

ans = a1_sums[0] - a2_sums[0]
for a1_s, a2_s in zip(a1_sums, a2_sums):
    ans = max(ans, a1_s-a2_s)
print(ans)
