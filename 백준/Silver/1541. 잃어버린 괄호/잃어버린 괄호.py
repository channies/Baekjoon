n = input().split('-')

num = []
for i in n:
    tmp = i.split('+')
    sum = 0
    for j in tmp:
        sum += int(j)
    num.append(sum)

ans = num[0]
for i in range(1, len(num)):
    ans -= num[i]
print(ans)
    