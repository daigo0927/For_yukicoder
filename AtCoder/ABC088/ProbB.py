n = int(input())
a = list(map(int, input().split()))

p_a = sum(sorted(a, reverse = True)[::2])
p_b = sum(a) - p_a
print(p_a - p_b)
