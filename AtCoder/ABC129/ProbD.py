# Refered #5850116 submit
import numpy as np

h, w = map(int, input().split())
s = np.array([list(input()) for _ in range(h)]) == '.'

ups = np.zeros((h, w), dtype = int)
downs = np.zeros((h, w), dtype = int)
lefts = np.zeros((h, w), dtype = int)
rights = np.zeros((h, w), dtype = int)

for i in range(1, h):
    ups[i] = (ups[i-1]+1)*s[i-1]
for i in range(h-2, -1, -1):
    downs[i] = (downs[i+1]+1)*s[i+1]
for j in range(1, w):
    lefts[:, j] = (lefts[:, j-1]+1)*s[:, j-1]
for j in range(w-2, -1, -1):
    rights[:, j] = (rights[:, j+1]+1)*s[:, j+1]
counts = ups+downs+lefts+rights
ans = np.max(counts*s)+1
print(ans)
