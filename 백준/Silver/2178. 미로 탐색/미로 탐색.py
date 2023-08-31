from collections import deque
import sys
input = sys.stdin.readline
arr = []
dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]

n, m = map(int, input().split())
for i in range(n):
    arr.append(list(map(int, input().rstrip())))
def bfs(x,y):
    q = deque()
    q.append((x,y))
    while q:
        x, y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < m and arr[nx][ny] == 1:
                q.append((nx, ny))
                arr[nx][ny] = arr[x][y] + 1
                
bfs(0,0)
print(arr[n-1][m-1])