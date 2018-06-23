# almost the copy of answer #2730510 

def S(n):
    return sum(list(map(int, str(n))))

def norm(n):
    return n/S(n)

k = int(input())
j = 1
order = 1
for i in range(k):
    print(j)
    if norm(j+10**(order-1)) > norm(j+10**(order)):
        order += 1
    j += 10**(order-1)
    
