N = int(input())
S = list(input())

change = S[1:].count('E')
min_ = change

for i in range(1, N):
    if S[i-1] == 'W':
        change += 1
    if S[i] == 'E':
        change -= 1
    if change < min_:
        min_ = change
print(min_)
        
    

