from collections import deque

a, b = map(int, input().split())

def bfs(a, b):
    q = deque()
    q.append((a,1))
    while q:
        temp, cnt = q.popleft()
        if temp == b:
            print(cnt)
            return
        if temp * 2 <= b:
            q.append((temp*2, cnt+1))
        if temp * 10 + 1 <= b:
            q.append((temp*10+1, cnt+1))
    print(-1)
        
bfs(a,b)
