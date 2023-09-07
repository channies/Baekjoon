n = int(input())
amount = []

for _ in range(n):
    w = int(input())
    if w == 0:
        amount.pop()
    else:
        amount.append(w)
        
print(sum(amount))