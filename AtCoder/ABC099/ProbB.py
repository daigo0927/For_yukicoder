a, b = map(int, input().split())

diff = b-a
ans = sum(list(range(diff))) - a
print(ans)
