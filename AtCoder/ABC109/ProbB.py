n = int(input())
ws = [input() for _ in range(n)]

ans = 'Yes'
w = ws[0]
end = w[-1]
w_map = {w:1}
for i in range(1, n):
    w_next = ws[i]
    if not w_next in w_map.keys():
        w_map[w_next] = 1
    else:
        ans = 'No'
        break
    if w_next[0] != end:
        ans = 'No'
        break
    w = w_next
    end = w[-1]
print(ans)
