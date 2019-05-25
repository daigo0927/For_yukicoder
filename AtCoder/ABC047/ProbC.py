s = input()

current = s[0]
ans = 0
for i in range(1, len(s)):
    if s[i] != current:
        ans += 1
        current = s[i]

print(ans)
