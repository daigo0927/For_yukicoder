MOD = 10**9+7
s = input()

cumsum = {}
for key in ['A', 'B', 'C', '?']:
    cumsum[key] = [0]*(len(s)+1)
for i, ss in enumerate(s):
    for key in cumsum.keys():
        if key == ss:
            cumsum[key][i+1] = cumsum[key][i]+1
        else:
            cumsum[key][i+1] = cumsum[key][i]

ans = 0
for i in range(1, len(s)-1):
    if s[i] == 'A' or s[i] == 'C':
        continue
    
    n_a = cumsum['A'][i]
    n_c = cumsum['C'][-1] - cumsum['C'][i+1]
    n_q_left = cumsum['?'][i]
    n_q_right = cumsum['?'][-1] - cumsum['?'][i+1]

    n_left = (n_a*pow(3, n_q_left, MOD))%MOD + (n_q_left*pow(3, max(n_q_left-1, 0), MOD))%MOD
    n_left %= MOD
    n_right = (n_c*pow(3, n_q_right, MOD))%MOD + (n_q_right*pow(3, max(n_q_right-1, 0), MOD))%MOD
    n_right %= MOD
    ans += (n_left*n_right)%MOD
    ans %= MOD

print(ans)
