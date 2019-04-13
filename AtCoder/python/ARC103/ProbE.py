s = input()
n = len(s)

if s[0] == '0' or s[-1] == '1':
    print(-1)
    exit()
for i in range(n-1):
    if s[i] != s[-2-i]:
        print(-1)
        exit()

path = {1:[v for v in range(2, n+1)]}

ans = []
u_cur, v_cur = 1, 2
n_prev = 0
for i in range(1, n//2):
    if s[i] == '1':
        for _ in range(i-n_prev):
            ans.append((u_cur, v_cur))
            v_cur += 1
        ans.append((v_cur, u_cur))
        u_cur, v_cur = v_cur, v_cur+1
        n_prev = i+1
for v in range(v_cur, n+1):
    ans.append((u_cur, v))
for a in ans:
    print(*a)
