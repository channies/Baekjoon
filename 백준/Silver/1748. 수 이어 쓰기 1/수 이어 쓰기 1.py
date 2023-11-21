n = int(input())

l = len(str(n))
cnt = 0

for i in range(l-1):
    cnt += 9 * (10 ** i) * (i+1)
cnt += (n- (10 ** (l-1))+1) * l

print(cnt)