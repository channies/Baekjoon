def solution(n, computers):
    
    def getParent(parent, x):
        if parent[x] == x:
            return x
        parent[x] = getParent(parent, parent[x])
        return parent[x]
    
    def unionParent(parent, x, y):
        x_p = getParent(parent, x)
        y_p = getParent(parent, y)
        
        if x_p < y_p:
            parent[y_p] = x_p
        else:
            parent[x_p] = y_p
        
    parent = [i for i in range(n)]
    
    for i in range(n):
        for j in range(n):
            if i != j and computers[i][j] == 1:
                unionParent(parent, i, j)
    
    answer = set()
    for i in range(n):
        answer.add(getParent(parent, i))
    return len(answer)