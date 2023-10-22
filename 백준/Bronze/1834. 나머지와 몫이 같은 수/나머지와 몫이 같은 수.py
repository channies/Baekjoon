n = int(input())
k = 1
answer = 0

while k < n:
    answer += n*k + k
    k += 1
    
print(answer)