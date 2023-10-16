def solution(routes):
    answer = 0
    routes.sort(key = lambda x: (x[1], x[0]))
    temp = -30001
    
    for k in routes:
        if k[0] > temp:
            answer += 1
            temp = k[1]
    return answer