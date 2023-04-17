완주하지 못한 선수

def solution(participant, completion):
    not_completion = {}
    for keys in participant:
        not_completion[keys] = not_completion.get(keys, 0) + 1
    for k in completion:
        not_completion[k] -= 1
    for i in not_completion:
        if not_completion[i] > 0:
            answer = i
    return answer
