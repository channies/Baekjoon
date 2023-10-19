import itertools

n = int(input())

for _ in range(n):
    arr = list(map(int, input().split()))
    comb = list(itertools.combinations(arr[1:], 2))
    ans = 0
    
    for k in comb:
        a, b = max(k[0], k[1]), min(k[0], k[1])
        while b:
            a, b = b, a % b
        ans += a
        
    print(ans)