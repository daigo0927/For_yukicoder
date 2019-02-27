s = int(input())

nums = set([s])
ans = 2
while True:
    s = s//2 if s%2 == 0 else 3*s+1
    if s in nums:
        print(ans)
        break
    else:
        nums.add(s)
        ans += 1
