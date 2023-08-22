import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

n, m = map(int, input().split())

cnt = 0
visited = [False] * (n+1)
arr = [[] for _ in range(n+1)]

for _ in range(m):
    u, v = map(int, input().split())
    arr[u].append(v)
    arr[v].append(u)
    
def dfs(s):
    visited[s] = True
    for i in arr[s]:
        if not visited[i]:
            dfs(i)
            
for i in range(1, n+1):
    if not visited[i]:
        dfs(i)
        cnt += 1
print(cnt)