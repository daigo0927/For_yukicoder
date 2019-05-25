s = input()
s = s[:-1]

while len(s) > 0:
    l = len(s)
    if l%2 == 1:
        s = s[:-1]
        continue
    if s[:l//2] == s[l//2:]:
        print(l)
        break
    else:
        s = s[:-1]
