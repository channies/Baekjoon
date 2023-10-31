import sys
input = sys.stdin.readline

n, m = map(int, input().split())
arr = []

for _ in range(n):
    arr.append(list(map(int, input().split())))

arr.sort(key = lambda x : (x[1],x[2],x[3]), reverse=True)
for i in range(n):
    if arr[i][0] == m:
        index = i
        
for i in range(n):
    if arr[index][1:] == arr[i][1:]:
        print(i+1)
        break