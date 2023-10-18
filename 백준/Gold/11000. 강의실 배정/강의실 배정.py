import heapq
import sys
input = sys.stdin.readline

n = int(input())
arr = []

for _ in range(n):
    s, t = map(int, input().split())
    arr.append((s,t))

arr.sort()
min_heap = list()
heapq.heappush(min_heap, arr[0][1])

for k in arr[1:]:
    if min_heap[0] <= k[0]:
        heapq.heappop(min_heap)
    heapq.heappush(min_heap, k[1])
    
print(len(min_heap))