n, m, c = map(int, input().split())
b = list(map(int, input().split()))

ans = 0
for _ in range(n):
    a = list(map(int, input().split()))
    ans += 1 if sum([aa*bb for aa, bb in zip(a, b)])+c > 0 else 0
print(ans)
