a, b = list(map(int, input().split()))
s = input().split('-')

if len(s) != 2:
    print('No')
elif len(s[0]) == a and len(s[1]) == b:
    print('Yes')
else:
    print('No')
