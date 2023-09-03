n = int(input())
dist = list(map(int, input().split()))
cost = list(map(int, input().split()))

min_cost = cost[0]
sum = 0

for i in range(n-1):
    if cost[i] < min_cost:
        min_cost = cost[i]
    sum += min_cost * dist[i]

print(sum)