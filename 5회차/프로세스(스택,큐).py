from collections import deque


def solution(priorities, location):
    answer = 1
    dq = deque(priorities)
    while len(dq) > 0:
        tmp = dq.popleft()
        if tmp < max(dq):
            dq.append(tmp)
            if location != 0:
                location -= 1
            else:
                location = len(dq)-1
        else:
            if location == 0:
                return answer
            else:
                answer += 1
                location -= 1
    return answer
