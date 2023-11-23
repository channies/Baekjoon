import sys
import heapq

input = sys.stdin.readline
mod = 10**9+9
n, m, s, e = map(int, input().split())
arr = [[] for _ in range(n+1)]
for _ in range(m):
    a, b, c = map(int, input().split())
    arr[a].append((b, c))
    arr[b].append((a, c))
    
INF = float('inf')
distance = [INF]*(n+1)
cnt = [0]*(n+1)
cnt[s] = 1


def dijkstra(x):
    q=[]
    heapq.heappush(q, (0,x))
    distance[x] = 0
    
    while q:
        dist, now = heapq.heappop(q)
        if distance[now] < dist:
            continue
            
        for k in arr[now]:
            cost = dist + k[1]
            if cost < distance[k[0]]:
                distance[k[0]] = cost
                heapq.heappush(q, (cost, k[0]))
                cnt[k[0]] = cnt[now]
            elif cost == distance[k[0]]:
                cnt[k[0]] = (cnt[k[0]] + cnt[now]) % mod
                
                
dijkstra(s)
print(cnt[e])