MOD = 10**9+7
n = int(input())
s1 = input()
s2 = input()

i = 0
ans = 1
pre_state = None
while i < n:
    if s1[i] == s2[i]:
        if pre_state == 'same':
            ans = (ans*2)%MOD
        elif pre_state == 'diff':
            pass
        else:
            ans = 3
        pre_state = 'same'
        i += 1
    elif s1[i] != s2[i]:
        if pre_state == 'same':
            ans = (ans*2)%MOD
        elif pre_state == 'diff':
            ans = (ans*3)%MOD
        else:
            ans = 6
        pre_state = 'diff'
        i += 2

print(ans)
