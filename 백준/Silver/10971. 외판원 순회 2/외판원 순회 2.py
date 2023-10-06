import sys
n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]
min_val = sys.maxsize

def dfs_backtracking(start, next, val, visited):
    global min_val
    
    if len(visited) == n:
        if arr[next][start] != 0:
            min_val = min(min_val, val + arr[next][start])
        return
    for i in range(n):
        if arr[next][i] != 0 and i not in visited and val < min_val:
            visited.append(i)
            dfs_backtracking(start, i, val + arr[next][i], visited)
            visited.pop()
            
for i in range(n):
    dfs_backtracking(i, i, 0, [i])
print(min_val)