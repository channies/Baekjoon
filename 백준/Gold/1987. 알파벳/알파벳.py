r, c = map(int, input().split())
arr = []
dx = [-1,1,0,0]
dy = [0,0,-1,1]
cnt = 1

for i in range(r):
    arr.append(list(input()))
        
def bfs(x,y):
    q = set()
    q.add((x,y,arr[x][y]))
    global cnt
    while q:
        x, y, visited = q.pop()
        cnt = max(cnt, len(visited))
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < r and 0 <= ny < c and arr[nx][ny] not in visited:
                q.add((nx,ny,visited+arr[nx][ny]))
bfs(0,0)
print(cnt)