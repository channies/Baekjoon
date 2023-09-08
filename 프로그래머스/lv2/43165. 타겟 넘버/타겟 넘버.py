from collections import deque

answer = 0

def solution(numbers, target):

    def bfs():
        global answer
        q = deque()
        q.append([numbers[0], 0])
        q.append([-numbers[0], 0])
        while q:
            temp, idx = q.popleft()
            idx += 1
            if idx < len(numbers):
                q.append([temp+numbers[idx], idx])
                q.append([temp-numbers[idx], idx])
            else:
                if temp == target:
                    answer += 1
            
    bfs()
    return answer