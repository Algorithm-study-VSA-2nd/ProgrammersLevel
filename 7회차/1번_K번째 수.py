def solution(array, commands):
    answer = []
    # answer에 넣을 빈 int 값 생성
    in_answer = 0
    for command in commands:
        # 조건에 맞는 변수들 생성
        i = command[0]
        j = command[1]
        k = command[2]
        # index에 맞게 -1 처리
        new_array = array[i-1:j]
        # 오름차순 분류
        new_array.sort()
        in_answer = new_array[k-1]
        answer.append(in_answer)
    return answer
