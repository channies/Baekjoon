import heapq
import sys
input = sys.stdin.readline

n = int(input())
max_heap = []

for _ in range(n):
    k = int(input())
    
    if k == 0:
        if max_heap:
            print(-heapq.heappop(max_heap))
        else:
            print(0)
    else:
        heapq.heappush(max_heap, -k)