n = int(input())
cnt = 0
for _ in range(n):
    stack = []
    word = input()
    for c in word:
        if stack and stack[-1] == c:
            stack.pop()
        else:
            stack.append(c)
    if not stack:
        cnt += 1
    
print(cnt)