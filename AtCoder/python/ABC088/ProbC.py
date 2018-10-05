c11, c12, c13 = list(map(int, input().split()))
c21, c22, c23 = list(map(int, input().split()))
c31, c32, c33 = list(map(int, input().split()))

ans = 'Yes'
if c12-c11 != c22-c21 or c22-c21 != c32-c31 or c32-c31 != c12-c11:
    ans = 'No'
if c13-c12 != c23-c22 or c23-c22 != c33-c32 or c33-c32 != c13-c12:
    ans = 'No'
if c21-c11 != c22-c12 or c22-c12 != c23-c13 or c23-c13 != c21-c11:
    ans = 'No'
if c31-c21 != c32-c22 or c32-c22 != c33-c23 or c33-c23 != c31-c21:
    ans = 'No'    
print(ans)
