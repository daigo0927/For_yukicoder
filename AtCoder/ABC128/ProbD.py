from collections import deque
from copy import deepcopy
import heapq

n, k = map(int, input().split())
v = list(map(int, input().split()))
v_sorted = sorted(v)

ans = 0
for i in range(k+1):
    for nl in range(i+1):
        nr = min(k - nl, n-nl)
        ansl, ansr = 0, 0
        for n_trash in range(nl):
            ansll, ansrr = 0, 0
            hands = sorted(v[:nl-n_trash])
            for vv in hands:
                if vv < 0 and n_trash > 0:
                    n_trash -= 1
                else:
                    ansll += vv
            ansl = max(ansl, ansll)

        for n_trash in range(nr):
            ansrr = 0
            hands = sorted(v[-(nr-n_trash):])
            # print(hands, nr, n_trash)
            for vv in hands:
                if vv < 0 and n_trash > 0:
                    n_trash -= 1
                else:
                    ansrr += vv
            ansr = max(ansr, ansrr)
        # print(ansl, ansr)
        ans = max(ans, ansl + ansr)

print(ans)
