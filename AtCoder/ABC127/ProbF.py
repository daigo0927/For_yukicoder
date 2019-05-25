from heapq import *

q = int(input())
b_cur = 0
diff = 0
lefts, rights = [], []

for i in range(q):
    query = input()
    if len(query) > 1:
        _, a, b = map(int, query.split())
        b_cur += b
        if len(lefts) == 0:
            heappush(lefts, -a)
        else:
            diff += abs(a + lefts[0])
            if a <= -lefts[0]:
                heappush(lefts, -a)
            else:
                heappush(rights, a)

        if len(lefts) < len(rights):
            med_r = heappop(rights)
            med_l = -lefts[0]
            diff += med_l - med_r
            heappush(lefts, -med_r)
        elif len(lefts) > len(rights)+1:
            med_l = -heappop(lefts)
            med_r = rights[0] if len(rights) > 0 else 0
            heappush(rights, med_l)
            
    else:
        print(-lefts[0], b_cur+diff)
            
