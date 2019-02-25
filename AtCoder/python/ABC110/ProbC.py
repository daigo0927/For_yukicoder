s = input()
t = input()

count_s = dict(zip([chr(i) for i in range(97, 97+26)], [0]*26))
count_t = dict(zip([chr(i) for i in range(97, 97+26)], [0]*26))
for ss, tt in zip(s, t):
    count_s[ss] += 1
    count_t[tt] += 1
v_s = sorted(count_s.values())
v_t = sorted(count_t.values())

ans = 'Yes' if v_s == v_t else 'No'
print(ans)
