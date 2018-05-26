N = int(input())
A = list(map(int, input().split(' ')))

def binxor(x, y):
    x = x.lstrip('0b')
    y = y.lstrip('0b')
    n = max(len(x), len(y))
    x = x.zfill(n)
    y = y.zfill(n)
    z = ''.join(list(map(str, [int(xx)^int(yy) for xx, yy in zip(x, y)])))
    return '0b0'+z

A10sum = [0]
Abinsum = [bin(0)]
for i in range(1, N+1):
    A10sum.append(A10sum[i-1]+A[i-1])
    Abinsum.append(binxor(Abinsum[i-1], bin(A[i-1])))
# print(f'10sum : {A10sum}')
# print(f'binsum : {Abinsum}')

count = 0
for l in range(1, N+1):
    for r in range(l, N+1):
        if(A10sum[r]-A10sum[l-1] == int(binxor(Abinsum[r], Abinsum[l-1]), 2)):
            count+=1
print(count)
