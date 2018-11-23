n = int(input())

if n%2 == 0:
    ans = 4*sum(list(range(n//2)))
else:
    ans = 4*sum(list(range(n//2)))+1
print(ans)
