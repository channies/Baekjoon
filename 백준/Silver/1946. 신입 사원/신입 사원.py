import sys
input = sys.stdin.readline
t = int(input())

for _ in range(t):
    n = int(input())
    arr = []
    for _ in range(n):
        x, y = map(int, input().split())
        arr.append((x,y))
        
    arr.sort()
    cnt = 1
    temp = arr[0][1]
    for i in range(1, n):
        if arr[i][1] < temp:
            cnt += 1
            temp = arr[i][1]
    print(cnt)
        