n, k = list(map(int, input().split()))
a = list(map(int, input().split()))

num_balls = [0]*(n+1)
for i in range(n):
    num_balls[a[i]] += 1
num_balls = sorted(num_balls, reverse = True)
# print(num_balls)

print(sum(num_balls[k:]))
