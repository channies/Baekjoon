ans = set()
arr = set()

for i in range(1, 10001):
    k = i
    ans.add(i)
    for n in str(i):
        k += int(n)
    arr.add(k)
        
ans = ans - arr
ans_s = sorted(ans)
for a in ans_s:
    print(a)