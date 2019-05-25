a, b, c, d = list(map(int, input().split()))

ans = max(0, min(b, d)-max(a, c))
print(ans)
