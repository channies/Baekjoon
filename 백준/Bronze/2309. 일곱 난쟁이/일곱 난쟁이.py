dwarfs = [int(input()) for _ in range(9)]

height_sum = sum(dwarfs) - 100
flag = 0
for i in range(0, 8):
    if flag == 1:
        break
    for j in range(i+1, 9):
        if dwarfs[i] + dwarfs[j] == height_sum:
            temp1 = dwarfs[i]
            temp2 = dwarfs[j]
            dwarfs.remove(temp1)
            dwarfs.remove(temp2)
            flag = 1
            break
            
dwarfs.sort()
for k in dwarfs:
    print(k)
    