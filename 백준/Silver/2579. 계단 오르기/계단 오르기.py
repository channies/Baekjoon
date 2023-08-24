n = int(input())
s = [0] * (n+1)
for i in range(1, n+1):
    s[i] = int(input())
dp = [0] * (n+1)

if n == 1:
    print(s[1])
    
elif n == 2:
    print(s[1] + s[2])

if n >= 3:
    dp[1] = s[1]
    dp[2] = s[1] + s[2]
    for i in range(3, n+1):
        dp[i] = max(s[i] + s[i-1] + dp[i-3], s[i] + dp[i-2])
    print(dp[n])