s = input()
a_idx, z_idx = 200000, 0

for i in range(len(s)):
    if s[i] == 'A':
        a_idx = min(i, a_idx)
    if s[i] == 'Z':
        z_idx = i
print(z_idx - a_idx + 1)
