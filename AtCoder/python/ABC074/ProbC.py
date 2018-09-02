a, b, c, d, e, f = list(map(int, input().split()))

water = {}
for i in range(f//(100*a)+1):
    for j in range(f//(100*b)+1):
        wtr = 100*a*i+100*b*j
        if wtr <= f and not wtr in water.keys():
            water[wtr] = 1
water = sorted(water.keys())[1:]

suger = {}
for i in range(f//c+1):
    for j in range(f//d+1):
        sgr = c*i+d*j
        if sgr <= f and not sgr in suger.keys():
            suger[sgr] = 1
suger = sorted(suger.keys())
# print(water, suger)

ans_w = 0
ans_s = 0
concent = 0
for wtr in water:
    for sgr in suger:
        if wtr+sgr > f:
            break
        if sgr > (wtr//100)*e:
            break
        if sgr/(sgr+wtr) >= concent:
            concent = sgr/(sgr+wtr)
            ans_w = wtr+sgr
            ans_s = sgr

print(ans_w, ans_s)
