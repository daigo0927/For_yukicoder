n = int(input())

fn = sum(list(map(int, list(str(n)))))
if n%fn == 0:
    print('Yes')
else:
    print('No')
