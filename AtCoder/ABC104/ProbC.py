d, g = list(map(int, input().split()))
pc = [list(map(int, input().split())) for _ in range(d)]

ans = 10**9
for bit in range(1<<d):
    score = 0
    n = 0
    
    for i in range(d): 
        if bit & 1<<i: # Problems completely answered
            score += pc[i][1] + pc[i][0]*100*(i+1)
            n += pc[i][0]

    if score >= g:
        ans = min(ans, n)
    else: # additional answering
        for i in range(d-1, -1, -1): # answer from high-score problem
            if bit & 1<<i: # already answered completely
                continue
            for j in range(pc[i][0]): # answer to remaining problems
                if score >= g:
                    break
                score += 100*(i+1)
                n += 1
        ans = min(ans, n)

print(ans)
