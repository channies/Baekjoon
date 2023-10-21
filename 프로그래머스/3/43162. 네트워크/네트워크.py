def solution(n, computers):
    answer = 0
    visited = [False] * n
    
    def dfs(x):
        visited[x] = True
        for i in range(n):
            if i != x and computers[x][i] == 1 and visited[i] == False:
                dfs(i)
    
    for com in range(n):
        if visited[com] == False:
            dfs(com)
            answer += 1
    return answer