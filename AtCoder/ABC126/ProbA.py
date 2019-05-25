n, k = map(int, input().split())
s = input()

ss = {'A':'a', 'B':'b', 'C':'c'}
print(s[:k-1]+ss[s[k-1]]+s[k:])
