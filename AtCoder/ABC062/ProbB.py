h, w = list(map(int, input().split()))
ans = [''.join(['#']*(w+2))]
for _ in range(h):
    ans.append('#'+input()+'#')
ans.append(''.join(['#']*(w+2)))

for a in ans:
    print(a)
