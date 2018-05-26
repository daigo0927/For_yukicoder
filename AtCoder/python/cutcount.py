N = input()
S = list(input())
max_ = 0
alphabets = [chr(i) for i in range(97, 97+26)]
for i in range(1, len(S)-1):
    x = S[:i]
    y = S[i:]
    match = 0
    for a in alphabets:
        if a in x and a in y:
            match += 1
    if match > max_:
        max_ = match
print(max_)

