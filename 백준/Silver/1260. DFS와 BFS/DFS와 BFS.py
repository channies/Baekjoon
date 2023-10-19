from collections import deque
import sys
input = sys.stdin.readline

n, m, v = map(int, input().split())
arr = [[] for _ in range(n+1)]
visited = []
visited_b = []

for _ in range(m):
    a, b = map(int, input().split())
    arr[a].append(b)
    arr[b].append(a)
    
for k in arr:
    k.sort()
    
def dfs(s):
    visited.append(s)
    for k in arr[s]:
        if k not in visited:
            dfs(k)
            
def bfs(s):
    q = deque()
    q.append(s)
    while q:
        s = q.popleft()
        visited_b.append(s)
        for k in arr[s]:
            if k not in visited_b and k not in q:
                q.append(k)
dfs(v)
bfs(v)

print(' '.join(map(str, visited)))
print(' '.join(map(str, visited_b)))