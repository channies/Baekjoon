from collections import deque

n = int(input())
q = deque()

for i in range(n):
    q.append(n-i)

while len(q) != 1:
    q.pop()
    q.appendleft(q.pop())
    
print(q.pop())
