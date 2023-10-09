n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]
prizes = []

for i in range(n):
    cnt = 1
    temp = arr[i][0]
    temp2 = arr[i][1]
    temp3 = arr[i][2]
    temp4 = arr[i][3]
    
    for j in range(1,4):
        if arr[i][j] == temp:
            cnt += 1
    if cnt == 4:
        prize = 50000+temp*5000
    elif cnt == 3:
        prize = 10000+temp*1000
    elif cnt == 2:
        if temp == temp2 and temp3 == temp4:
            prize = 2000+temp*500+temp3*500
        elif temp == temp3 and temp2 == temp4:
            prize = 2000+temp*500+temp2*500
        elif temp == temp4 and temp3 == temp2:
            prize = 2000+temp*500+temp3*500            
        elif (temp == temp2 and temp3 != temp4) or (temp == temp3 and temp2 != temp4) or (temp == temp4 and temp3 != temp2):
            prize = 1000+temp*100        
    else:
        if temp2 == temp3 == temp4:
            prize = 10000+temp2*1000
        elif (temp2 == temp3 and temp3!= temp4) or (temp2 == temp4 and temp4!= temp3):
            prize = 1000+temp2*100
        elif temp2 != temp3 and temp3 == temp4:
            prize = 1000+temp3*100
        else:
            prize = max(arr[i])*100
    prizes.append(prize)
    
print(max(prizes))