N, D = list(map(int, input().split(' ')))
X = list(map(int, input().split(' ')))

# 右側徒歩圏内
R = [0]*N
r_i = 0
count = 0
for l_i in range(N):
    while r_i < N and X[r_i] - X[l_i] <= D:
        count += 1
        r_i += 1
    R[l_i] = count-1
    count -= 1

L = [0]*N
# X_ = X[::-1]
# r_i = 0
# count = 0
# for l_i in range(N):
#     while r_i < N and abs(X_[r_i] - X_[l_i]) <= D:
#         count += 1
#         r_i += 1
#     L[l_i] = count-1
#     count -= 1
# L = L[::-1]
l_i = N-1
count = 0
for r_i in range(N-1, -1, -1):
    while l_i >= 0 and X[r_i] - X[l_i] <= D:
        count += 1
        l_i -= 1
    L[r_i] = count-1
    count -= 1

# print(R, L)

A = 0
for i in range(N):
    A += L[i]*(L[i]-1)//2

B = 0
for j in range(1, N-1):
    B += L[j]*R[j]

print(B - A)
                
