from itertools import permutations

n, k = map(int, input().split())
arr = [i+1 for i in range(n)]
ans = list(permutations(arr, k))

for i in range(k):
    ans.sort(key = lambda x: x[k-1-i])
    
for answer in ans:
    print(' '.join(map(str, answer)))
