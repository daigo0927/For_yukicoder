s = input()
k = int(input())

k = min(k, len(s))
for i in range(k):
    if int(s[i]) != 1:
        print(s[i])
        break
    if i == k-1 and int(s[i]) == 1:
        print(1)
        break
