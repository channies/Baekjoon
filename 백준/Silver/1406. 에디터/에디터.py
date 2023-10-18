from collections import deque
import sys
input = sys.stdin.readline

arr = input().rstrip()
q_left = deque([k for k in arr])
n = int(input())
result = []
q_right = deque()

for _ in range(n):
    com = list(input().split())
    if com[0] == 'L' and q_left:
        q_right.appendleft(q_left.pop())
    elif com[0] == 'D' and q_right:
        q_left.append(q_right.popleft())
    elif com[0] == 'B' and q_left:
        q_left.pop()
    elif com[0] == 'P':
        q_left.append(com[1])
        
result = q_left+q_right
print(''.join(result))
        