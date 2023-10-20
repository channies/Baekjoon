import sys
input = sys.stdin.readline

n = int(input())
arr = list(map(int, input().split()))
ans = []
dp = [0] * n
dp[0] = arr[0]

for i in range(1, n):
    dp[i] = max(arr[i], dp[i-1]+arr[i])
    if dp[i] < dp[i-1]:
        ans.append(dp[i-1])
        
if ans:
    print(max(ans))
else:
    print(max(dp))
    
