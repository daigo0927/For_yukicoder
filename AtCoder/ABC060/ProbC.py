n, T = list(map(int, input().split()))
t = list(map(int, input().split()))

end = T
ans = T
for i in range(1, n):
    if t[i] < end:
        ans = ans - (end-t[i]) + T
    else:
        ans += T
    end = t[i] + T
    
print(ans)
