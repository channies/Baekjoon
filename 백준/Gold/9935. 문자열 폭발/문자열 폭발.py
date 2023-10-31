import sys
input = sys.stdin.readline

arr = input().rstrip()
bomb = input().rstrip()
stack = []
m = len(bomb)

for k in arr:
    stack.append(k)
    if ''.join(stack[-m:]) == bomb:
        for _ in range(m):
            stack.pop()
            
if stack:
    print(''.join(stack))
else:
    print("FRULA")
    