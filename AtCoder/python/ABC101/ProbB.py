n = int(input())

sn = sum(list(map(int, list(str(n)))))
ans = 'Yes' if n%sn == 0 else 'No'
print(ans)
