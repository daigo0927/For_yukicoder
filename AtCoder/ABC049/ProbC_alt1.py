s = input()
stack = []
choices = ['dream', 'dreamer', 'erase', 'eraser']
for c in choices:
    if s[:len(c)] == c:
        stack.append(len(c))

ans = 'NO'
while len(stack) > 0:
    i = stack[-1]
    # print(stack, i)
    stack = stack[:-1]
    if i == len(s):
        ans = 'YES'
        break
    for c in choices:
        if s[i:i+len(c)] == c:
            stack.append(i+len(c))
                
print(ans)
        
