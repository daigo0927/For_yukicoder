s_ = input()
t = input()

answers = []
for i in range(len(s_)-len(t)+1):
    ans = s_
    for j in range(len(t)):
        matched = True
        if s_[i+j] != t[j] and s_[i+j] != '?':
            matched = False
            break
        else:
            ans = ans[:i+j] + t[j] + ans[i+j+1:]
    if matched:
        ans = ans.replace('?', 'a')
        answers.append(ans)
# print(answers)

if len(answers) == 0:
    print('UNRESTORABLE')
else:
    print(sorted(answers)[0])
