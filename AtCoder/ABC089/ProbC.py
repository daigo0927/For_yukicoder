n = int(input())
s = [input() for _ in range(n)]

keys = ['M', 'A', 'R', 'C', 'H']
chars = dict(zip(keys, [0]*5))
for i in range(n):
    if s[i][0] in keys:
        chars[s[i][0]] += 1
# print(chars)

ans = 0
for i in range(1<<5):
    if bin(i).count('1') != 3:
        continue
    num = 1
    for j in range(5):
        if i&1 == 1:
            num *= chars[keys[j]]
        i >>= 1
    ans += num
print(ans)
