k = int(input())

print(50)
ans = [49+k//50]*50
for i in range(50):
    if i < k%50:
        ans[i] = ans[i]+50-(k%50-1)
    else:
        ans[i] -= k%50
print(' '.join(list(map(str, ans))))
