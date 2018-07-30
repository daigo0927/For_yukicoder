x = int(input())

i = 1
ans = 0
while True:
    ans += i
    if ans >= x:
        print(i)
        break
    i += 1
