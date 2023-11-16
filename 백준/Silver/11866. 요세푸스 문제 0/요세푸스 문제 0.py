from collections import deque

n, k = map(int, input().split())

q = deque()
for i in range(1, n+1):
    q.append(i)
    
ans = []    
while q:
    for _ in range(k-1):
        if q:
            q.append(q.popleft())
        else:
            break
    ans.append(q.popleft())
    
print("<" + ', '.join(map(str, ans)) + ">")