s = input()

string = 'keyence'
if s[-7:] == string:
    ans = 'YES'
elif s[:7] == string:
    ans = 'YES'
else:
    ans = 'NO'
    for i in range(1, 7):
        if s[:i] == string[:i] and s[-(7-i):] == string[-(7-i):]:
            ans = 'YES'
            break
print(ans)
        
    
