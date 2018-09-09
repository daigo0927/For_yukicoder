n, m = list(map(int, input().split()))

ans = (100*(n-m)+1900*m)*(2**m)
print(ans)
