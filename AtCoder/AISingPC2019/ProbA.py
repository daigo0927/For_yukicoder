n = int(input())
h = int(input())
w = int(input())

ans = (n-h+1)*(n-w+1)
print(max(0, ans))
