n, k = map(int, input().split())
number = input()
cnt = 0
stack = []

for num in number:
    while cnt < k and stack and stack[-1] < num:
        stack.pop()
        cnt += 1
    stack.append(num)

if cnt != k:
    stack = stack[:-(k-cnt)]
print(''.join(stack))