n = int(input())
l = list(map(int, input().split()))

ans = 'Yes' if max(l) < sum(l)-max(l) else 'No'
print(ans)
