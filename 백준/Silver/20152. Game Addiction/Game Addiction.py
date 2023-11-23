h,n=map(int,input().split())

m=abs(h-n)+1
arr = [[0] * m for _ in range(m)]
for i in range(m):
    arr[0][i] = 1
    
for i in range(1, m):
    for j in range(i,m):
        arr[i][j] = arr[i-1][j] + arr[i][j-1]
        
print(arr[-1][-1])