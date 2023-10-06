import sys
import copy

n, m = map(int, input().split())
arr = []
cctvs = []
mode = [
    [],
    [[0], [1], [2], [3]],
    [[0,1], [2,3]],
    [[0,3], [1,3], [1,2], [0,2]],
    [[0,1,2], [0,1,3], [0,2,3], [1,2,3]],
    [[0,1,2,3]]
]
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
min_val = sys.maxsize

for i in range(n):
    data = list(map(int, input().split()))
    arr.append(data)
    for j in range(m):
        if data[j] in [1, 2, 3, 4, 5]:
            cctvs.append([data[j], i, j])

def search(arr, mode, x, y):
    for i in mode:
        nx = x
        ny = y
        while True:
            nx += dx[i]
            ny += dy[i]
            if nx < 0 or ny < 0 or nx >= n or ny >= m:
                break
            if arr[nx][ny] == 6:
                break
            elif arr[nx][ny] == 0:
                arr[nx][ny] = -1
                
def dfs(arr, depth):
    global min_val
    if depth == len(cctvs):
        cnt = 0
        for i in range(n):
            cnt += arr[i].count(0)
        min_val = min(min_val, cnt)
        return
    temp = copy.deepcopy(arr)
    cctv, x, y = cctvs[depth]
    for i in mode[cctv]:
        search(temp, i, x, y)
        dfs(temp, depth+1)
        temp = copy.deepcopy(arr)
        
dfs(arr, 0)
print(min_val)