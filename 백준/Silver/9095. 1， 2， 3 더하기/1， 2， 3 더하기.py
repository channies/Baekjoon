n = int(input())

for m in range(n):
    m = int(input())
    dp = [0] * (m+1)
    if m == 1:
        print(1)
    elif m == 2:
        print(2)
    elif m == 3:
        print(4)
    else:
        dp[1] = 1
        dp[2] = 2
        dp[3] = 4
        for i in range(4, m+1):
            dp[i] = dp[i-1] + dp[i-2] + dp[i-3]
        print(dp[m])