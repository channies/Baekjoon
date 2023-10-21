def solution(begin, target, words):
    ans = []
    visited = [False] * len(words)
    
    def diff_check(a,b):
        k = 0
        for i in range(len(a)):
            if a[i] == b[i]:
                k += 1
        if k == len(a)-1:
            return True
        else:
            return False
        
    def dfs(x, cnt):
        if x == target:
            ans.append(cnt)
            return
        
        for i in range(len(words)):
            if diff_check(words[i], x):
                if not visited[i]:
                    visited[i] = True
                    dfs(words[i], cnt+1)
                    visited[i] = False
                    
    dfs(begin, 0)

    return min(ans) if ans else 0