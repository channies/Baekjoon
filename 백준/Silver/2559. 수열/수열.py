import sys
input = sys.stdin.readline

n, k = map(int, input().split())
arr = list(map(int, input().split()))
ans = sum(arr[:k])
temp = sum(arr[:k])

for i in range(1, n-k+1):
    temp += -arr[i-1]+arr[i+k-1]
    ans = max(ans, temp)
print(ans)