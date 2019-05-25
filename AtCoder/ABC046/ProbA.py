abc = list(map(int, input().split()))
penki = {}
for i in range(3):
    if not abc[i] in penki.keys():
        penki[abc[i]] = 1
    else:
        continue
print(len(penki.keys()))
    
