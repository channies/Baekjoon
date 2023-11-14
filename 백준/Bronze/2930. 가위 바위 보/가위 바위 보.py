n = int(input())
arr = input()
m = int(input())

comp = []
for _ in range(m):
    comp.append(input())

rsp = {'R': 0, 'S': 1, 'P': 2}
result = 0
cnt = 0

for i in range(n):
    case = [['R', 0], ['S', 0], ['P', 0]]
    for j in range(m):
        if (rsp[arr[i]] + 1) % 3 == rsp[comp[j][i]]:
            cnt += 2
        elif arr[i] == comp[j][i]:
            cnt += 1
            
        for rsp_case in case:
            if (rsp[rsp_case[0]] + 1) % 3 == rsp[comp[j][i]]:
                rsp_case[1] += 2
            elif rsp_case[0] == comp[j][i]:
                rsp_case[1] += 1
    result += max(case, key=lambda x: x[1])[1]
    
print(cnt)
print(result)