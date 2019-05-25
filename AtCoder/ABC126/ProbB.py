s = input()

def is_yymm(s):
    y, m = int(s[:2]), int(s[2:])
    return True if m > 0 and m < 13 else False

def is_mmyy(s):
    m, y = int(s[:2]), int(s[2:])
    return True if m > 0 and m < 13 else False

if is_yymm(s) and is_mmyy(s):
    print('AMBIGUOUS')
elif is_yymm(s) and not is_mmyy(s):
    print('YYMM')
elif not is_yymm(s) and is_mmyy(s):
    print('MMYY')
else:
    print('NA')
