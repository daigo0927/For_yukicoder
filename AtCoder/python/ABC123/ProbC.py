n = int(input())
a = [int(input()) for _ in range(5)]

ans = n//min(a) if n%min(a) == 0 else n//min(a)+1
print(ans+4)
