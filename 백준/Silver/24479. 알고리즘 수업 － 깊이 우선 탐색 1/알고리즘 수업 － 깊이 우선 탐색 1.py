import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**8)

n, m, r = map(int, input().split())
arr = [[] for _ in range(n+1)]
v = [0] * (n+1)
cnt = 0

for _ in range(m):
    a, b = map(int, input().split())
    arr[a].append(b)
    arr[b].append(a)
    
for k in arr:
    k.sort()
    
def dfs(x):
    global cnt
    cnt += 1
    v[x] = cnt
    for k in arr[x]:
        if v[k] == 0:
            dfs(k)
dfs(r)

for k in v[1:]:
    print(k)