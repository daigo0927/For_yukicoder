n, k = list(map(int, input().split(' ')))
a = list(map(int, input().split(' ')))
# print(n, k, a)
if n == k:
    print(1)
elif (n-k)%(k-1) == 0:
    print((n-k)//(k-1)+1)
else:
    print((n-k)//(k-1)+2)

# for i, aa in enumerate(a):
#     if aa == 1:
#         min_idx = i
#         break

# num_ops = [0]*k
# for i in range(k):
#     left_remain = max(0, min_idx-(k-1)+i)
#     right_remain = max(0, n-min_idx-k-i)
#     num_ops[i] += 1

#     if left_remain%(k-1) > 0:
#         num_ops[i] += left_remain//(k-1)+1
#     else:
#         num_ops[i] += left_remain//(k-1)
#         # print(num_operate)
#     if right_remain%(k-1) > 0:
#         num_ops[i] += right_remain//(k-1)+1
#     else:
#         num_ops[i] += right_remain//(k-1)
    

# print(min(num_ops))
