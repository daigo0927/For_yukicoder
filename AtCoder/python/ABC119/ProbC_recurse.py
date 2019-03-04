inf = 10**9
n, a, b, c = map(int, input().split())
l = [int(input()) for _ in range(n)]

def dfs(i, a_cur, b_cur, c_cur):
    if i == n:
        return abs(a_cur-a) + abs(b_cur-b) + abs(c_cur-c) - 30 if min(a_cur, b_cur, c_cur) > 0 else inf
    ans0 = dfs(i+1, a_cur+l[i], b_cur, c_cur) + 10
    ans1 = dfs(i+1, a_cur, b_cur+l[i], c_cur) + 10
    ans2 = dfs(i+1, a_cur, b_cur, c_cur+l[i]) + 10
    ans3 = dfs(i+1, a_cur, b_cur, c_cur)
    return min(ans0, ans1, ans2, ans3)

print(dfs(0, 0, 0, 0))
