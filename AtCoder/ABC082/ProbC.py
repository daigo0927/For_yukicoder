n = int(input())
a = list(map(int, input().split()))

nums = {}
for i in range(n):
    if not a[i] in nums.keys():
        nums[a[i]] = 1
    else:
        nums[a[i]] += 1

ans = 0
for k in nums.keys():
    if nums[k] > k:
        ans += nums[k]-k
    elif nums[k] < k:
        ans += nums[k]
print(ans)
