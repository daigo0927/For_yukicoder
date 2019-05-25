import heapq
x, y, z, k = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))
c = list(map(int, input().split()))

a = sorted([-aa for aa in a])
b = sorted([-bb for bb in b])
c = sorted([-cc for cc in c])
a_diff = [a[i+1]-a[i] for i in range(x-1)]
b_diff = [b[i+1]-b[i] for i in range(y-1)]
c_diff = [c[i+1]-c[i] for i in range(z-1)]

que = [(a[0]+b[0]+c[0], (0, 0, 0))]
heapq.heapify(que)
s = set([(0, 0, 0)])
while k > 0:
    ans, (ia, ib, ic) = heapq.heappop(que)
    print(-ans)
    # print(-ans, (ia, ib, ic))
    k -= 1

    if ia < x-1 and (ia+1, ib, ic) not in s:
        heapq.heappush(que, (ans+a_diff[ia], (ia+1, ib, ic)))
        s.add((ia+1, ib, ic))
    if ib < y-1 and (ia, ib+1, ic) not in s:
        heapq.heappush(que, (ans+b_diff[ib], (ia, ib+1, ic)))
        s.add((ia, ib+1, ic))
    if ic < z-1 and (ia, ib, ic+1) not in s:
        heapq.heappush(que, (ans+c_diff[ic], (ia, ib, ic+1)))
        s.add((ia, ib, ic+1))
