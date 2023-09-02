import sys
from collections import deque

n = int(sys.stdin.readline())
que = deque()

for i in range(n):
    command = sys.stdin.readline().split()
    if command[0] == 'push':
        que.append(command[-1])
    elif command[0] == 'pop':
        if que:
            print(que.popleft())
        else:
            print(-1)
    elif command[0] == 'size':
        print(len(que))
    elif command[0] == 'empty':
        if not que:
            print(1)
        else:
            print(0)
    elif command[0] == 'front':
        if que:
            print(que[0])
        else:
            print(-1)
    elif command[0] == 'back':
        if que:
            print(que[-1])
        else:
            print(-1)