import heapq
s = input()
k = int(input())

que = []
heapq.heapify(que)
subs = set([])
for char in range(97, 97+26):
    char = chr(char)
    for i, ss in enumerate(s):
        if ss == char:
            heapq.heappush(que, (ss, i))
    while len(que) > 0:
        sub, i = heapq.heappop(que)
        if not sub in subs:
            subs.add(sub)
            k -= 1
            # print(sub)
            if k == 0:
                print(sub)
                exit()
        
        i_end = i+len(sub)+1
        if i_end > len(s):
            continue
        else:
            heapq.heappush(que, (s[i:i+len(sub)+1], i))
