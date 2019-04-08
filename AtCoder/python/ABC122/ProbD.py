from collections import defaultdict
MOD = 10**9+7
n = int(input())

basis = ['A', 'C', 'G', 'T']
cands = {}
for i in basis:
    for j in basis:
        for k in basis:
            ijk = i+j+k
            if ijk in ['AGC', 'GAC', 'ACG']:
                cands[ijk] = 0
            else:
                cands[ijk] = 1
for i in range(3, n):
    cands_tmp = {ijk:0 for ijk in cands.keys()}
    for k, v in cands.items():
        for l in basis:
            k_new = k+l
            if k_new[1:] in ['AGC', 'GAC', 'ACG']:
                pass
            elif k_new[0] == 'A' and 'G' in k_new[1:3] and k_new[3] == 'C':
                pass
            else:
               cands_tmp[k_new[1:]] += v
               cands_tmp[k_new[1:]] %= MOD
    cands = cands_tmp
    
print(sum(cands.values())%MOD)
    
