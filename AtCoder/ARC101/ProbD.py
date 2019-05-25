n = int(input())
a = list(map(int, input().split()))

a_sorted = sorted(set(a))+[10**18]
left, right = 0, len(a_sorted)-1

while right-left > 1:
    mid = (left+right)//2
    x = a_sorted[mid]

    count = [0]*(2*n+1)
    count[n+1] = 1
    i, accum, res = n+1, 1, 0

    for aa in a:
        if aa >= x:
            i += 1
            accum += count[i]
        else:
            accum -= count[i]
            i -= 1

        res += accum
        count[i] += 1
        accum += 1

    if res >= n*(n+1)//4:
        left = mid
    else:
        right = mid

print(a_sorted[left])
