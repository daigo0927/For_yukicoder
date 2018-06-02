A, B, N = list(map(int, input().split(' ')))
X = list(input())

for x in X:
    if x == 'S':
        A = max(0, A-1)
    elif x == 'C':
        B = max(0, B-1)
    else:
        if A>=B:
            A = max(0, A-1)
        else:
            B = max(0, B-1)
print(A)
print(B)
