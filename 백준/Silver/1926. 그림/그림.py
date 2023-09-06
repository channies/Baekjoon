import sys
sys.setrecursionlimit(10 ** 6)

from collections import deque

n, m = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
ans = []
a = 0
            
def bfs(xs,ys):
    q = deque()
    q.append((xs,ys))
    cnt = 1
    arr[xs][ys] = 0    
    while q:
        x, y = q.pop()
        for i in range(4):
            nx = x+dx[i]
            ny = y+dy[i]
            if 0 <= nx < n and 0 <= ny < m and arr[nx][ny] == 1:
                q.append((nx,ny))
                arr[nx][ny] = 0
                cnt += 1
    return cnt

for i in range(n):
    for j in range(m):
        if arr[i][j] == 1:
            cnt = bfs(i,j)
            a += 1
            ans.append(cnt)
            
if ans:
    print(a)
    print(max(ans))
else:
    print(0)
    print(0)