n = int(input())
m = int(input())

visited = [0] * (n+1)
graph = [[] for _ in range(n+1)]

cnt = 0

for i in range(m):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)
    
def dfs(x):
    global cnt
    visited[x] = 1
    cnt += 1
    for k in graph[x]:
        if visited[k] == 0:
            dfs(k)
            
dfs(1)
print(cnt - 1)