import sys
input = sys.stdin.readline

n = int(input())
m = int(input())
arr = []

for _ in range(m):
    a, b, cost = map(int, input().split())
    arr.append((cost, a, b))
    
arr.sort()

parent = [0] * (n+1)
for i in range(n+1):
    parent[i] = i

def findParent(parent, x):
    if parent[x] != x:
        parent[x] = findParent(parent, parent[x])
    return parent[x]

def unionParent(parent, a, b):
    a = findParent(parent, a)
    b = findParent(parent, b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b
        
result = 0       
for k in arr:
    cost, a, b = k
    if findParent(parent, a) != findParent(parent, b):
        unionParent(parent, a, b)
        result += cost
        
print(result)