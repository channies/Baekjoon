import sys
sys.setrecursionlimit(10000)

n = int(input())

def dfs(node):
    visited[node] = True
    next_node = graph[node]
    if not visited[next_node]:
        dfs(next_node)

for i in range(n):
    m = int(input())
    graph = [0] + list(map(int, input().split()))
    visited = [False] * (m+1)
    cnt = 0
    for i in range(1, m+1):
        if not visited[i]:
            dfs(i)
            cnt += 1

    print(cnt)
            
        
    