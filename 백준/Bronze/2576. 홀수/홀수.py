odd = []

for _ in range(7):
    k = int(input())
    if k % 2 == 0:
        continue
    else:
        odd.append(k)
        
if len(odd) != 0:
    print(sum(odd))
    print(min(odd))
else:
    print(-1)