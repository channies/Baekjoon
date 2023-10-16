def solution(targets):
    answer = 0
    targets.sort(key = lambda x: (x[1], x[0]))
    temp = 0
    
    for k in targets:
        if k[0] < temp:
            continue
        else:
            answer += 1
            temp = k[1]
    
    return answer