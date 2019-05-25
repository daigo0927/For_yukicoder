s = input()

num = {}
for ss in s:
    num[ss] = 1

ans = 'None'
for i in range(97, 97+26):
    if not chr(i) in num.keys():
        ans = chr(i)
        break
print(ans)
    
