n = int(input())
s = [input() for _ in range(n)]
m = int(input())
t = [input() for _ in range(m)]

words = {}
for i in range(n):
    if not s[i] in words.keys():
        words[s[i]] = 1
    else:
        words[s[i]] += 1
for i in range(m):
    if not t[i] in words.keys():
        words[t[i]] = -1
    else:
        words[t[i]] -= 1

ans = 0
for k, v in words.items():
    ans = max(ans, v)
print(ans)
