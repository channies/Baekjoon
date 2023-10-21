import heapq
import sys
input = sys.stdin.readline
INF = sys.maxsize

v, e = map(int, input().split())
s = int(input())
arr = [[] for _ in range(v+1)]
distance = [INF] * (v+1)

for _ in range(e):
    a, b, w = map(int, input().split())
    arr[a].append((w,b))
    
def dijkstra(s):
    q = []
    heapq.heappush(q, (0, s))
    distance[s] = 0
    
    while q:
        dist, x = heapq.heappop(q)
        if dist > distance[x]:
            continue
        for i in arr[x]:
            cost = dist+i[0]
            if cost < distance[i[1]]:
                distance[i[1]] = cost
                heapq.heappush(q, (cost, i[1]))
                
dijkstra(s)

for i in range(1, v+1):
    if distance[i] == INF:
        print("INF")
    else:
        print(distance[i])
            