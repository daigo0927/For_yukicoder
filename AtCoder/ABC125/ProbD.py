n = int(input())
a = list(map(int, input().split()))

n_neg = sum([1 for i in range(n) if a[i] < 0])
if n_neg%2 == 0:
    ans = sum([abs(aa) for aa in a])
else:
    min_abs = min([abs(aa) for aa in a])
    ans = sum([abs(aa) for aa in a]) - 2*min_abs
print(ans)
