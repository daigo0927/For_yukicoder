n, k = map(int, input().split())
s = input()
if set(list(s)) == 1:
    print(n)
    exit

s = '0' + s + '0'
list_ones = []
for i in range(1, n+1):
    if s[i-1] == '0' and s[i] == '1':
        i_start = i
    if s[i] == '1' and s[i+1] == '0':
        i_end = i
        list_ones.append((i_start, i_end))
list_ones = [(1, 1)] + list_ones + [(n, n)]
# print(list_ones)

ans = 0
for j, (i_start, _) in enumerate(list_ones):
    j_end = min(len(list_ones)-1, j+k)
    _, i_end = list_ones[j_end]
    ans = max(ans, i_end-i_start+1)
print(ans)
