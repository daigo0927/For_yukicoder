n = int(input())
h = list(map(int, input().split()))

ans = 0
watering = False
while sum(h) > 0:
    for i in range(n):
        if h[i] > 0:
            if not watering:
                ans += 1
            watering = True
            h[i] -= 1
        else:
            watering = False
    watering = False
print(ans)
