n = int(input())
v = list(map(int, input().split()))
c = list(map(int, input().split()))

ans = sum([max(vv-cc, 0) for vv, cc in zip(v, c)])
print(ans)
