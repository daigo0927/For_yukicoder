n = int(input())

if n%111 == 0:
    print(n)
else:
    print(111*(n//111+1))
