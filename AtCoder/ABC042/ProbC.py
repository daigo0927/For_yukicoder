n, k = list(map(int, input().split()))
d = list(map(int, input().split()))
while(True):
    contain = False
    for nn in str(n):
        if int(nn) in d:
            contain = True
            n += 1
            break
    if not contain:
        break
        
print(n)
