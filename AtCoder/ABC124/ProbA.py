a, b = map(int, input().split())

a, b = max(a, b), min(a, b)
ans = 2*a-1 if a-b > 1 else a+b
print(ans)
