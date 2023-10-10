n = int(input())
arr = [int(input()) for _ in range(n)]
stack = []
ans  =[]
i, j = 1, 0

while True:
    if stack and stack[-1] == arr[j]:
        stack.pop()
        ans.append('-')
        j += 1
    else:
        if i > n:
            break
        stack.append(i)
        ans.append('+')
        i += 1
        
if stack:
    print('NO')
else:
    for k in ans:
        print(k)