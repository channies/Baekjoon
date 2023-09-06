import sys
sys.setrecursionlimit(10**6)

n, m = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
ans = []
            
def dfs(x,y):
    global cnt
    arr[x][y] = 0
    cnt += 1
    for i in range(4):
        nx = x+dx[i]
        ny = y+dy[i]
        if 0 <= nx < n and 0 <= ny < m and arr[nx][ny] == 1:
            dfs(nx,ny)
   
    
for i in range(n):
    for j in range(m):
        if arr[i][j] == 1:
            cnt = 0
            dfs(i,j)
            ans.append(cnt)
            
if ans:
    print(len(ans))
    print(max(ans))
else:
    print(0)
    print(0)