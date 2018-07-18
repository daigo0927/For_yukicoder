s = input()

ans = {0:'Second', 1:'First'}
if s[0] == s[-1]:
    print(ans[(len(s)-1)%2])
else:
    print(ans[len(s)%2])
