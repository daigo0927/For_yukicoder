n, m, X, Y = map(int, input().split())
x = list(map(int, input().split()))
y = list(map(int, input().split()))

ans = 'No War' if max([X]+x) < min([Y]+y) else 'War'
print(ans)
