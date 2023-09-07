n, m = map(int, input().split())
x, y, d = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]

dx =[-1, 0, 1, 0]
dy = [0, 1, 0, -1]

def dfs(x,y,d):
    global cnt
    if arr[x][y] == 0:
        arr[x][y] = 2
        cnt += 1    
    for _ in range(4):
        nd = (d+3) % 4
        nx = x + dx[nd]
        ny = y + dy[nd]
        
        if arr[nx][ny] == 0:
            dfs(nx,ny,nd)
            return
        d = nd
    nd = (d+2) % 4
    nx = x + dx[nd]
    ny = y + dy[nd]
    if arr[nx][ny] == 1:
        return
    dfs(nx,ny,d)
cnt = 0
  
dfs(x,y,d)
print(cnt)
            
        