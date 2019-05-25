s = input()
n = len(s)

n_0 = sum([1 for ss in s if ss == '0'])
diff = abs(n_0 - (n-n_0))
print(n - diff)
