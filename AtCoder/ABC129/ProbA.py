p, q, r = map(int, input().split())

ans = sum([p, q, r]) - max(p, q, r)
print(ans)
