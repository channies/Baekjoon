N, K = map(int, input().split())
coins = []
for _ in range(N):
    coins.append(int(input()))
coins.sort(reverse=True)
cnt = 0
for coin in coins:
    if coin <= K:
        cnt += K // coin
        K %= coin
        if K == 0:
            break
print(cnt)