from itertools import permutations

n, k = map(int, input().split())
arr = [i+1 for i in range(n)]
ans = list(permutations(arr, k))

for answer in ans:
    print(' '.join(map(str, answer)))
