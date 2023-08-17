n = int(input())
arr = [list(map(int, input())) for _ in range(n)]

dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]

ans = []
num = 0

def dfs(x,y):
    global cnt
    if (x >= 0 and x < n and y < n and y >= 0 and arr[x][y] == 1):
        cnt += 1
        arr[x][y] = 0
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            dfs(nx, ny)
            
for i in range(n):
    for j in range(n):
        if arr[i][j] == 1:
            cnt = 0
            dfs(i, j)
            ans.append(cnt)
            num += 1
        
ans.sort()
print(num)
for i in ans:
    print(i)
