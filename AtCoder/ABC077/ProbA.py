c1 = input()
c2 = input()

ans = 'YES'
for i in range(3):
    if c1[i] != c2[-(i+1)]:
        ans = 'NO'
        break
print(ans)
