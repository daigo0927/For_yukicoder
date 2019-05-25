s = input().split()

ans = ''
for ss in s:
    ans += chr(ord(ss[0])-32)
print(ans)
