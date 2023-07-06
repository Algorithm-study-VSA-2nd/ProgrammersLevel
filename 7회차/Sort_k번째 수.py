# array=[1, 5, 2, 6, 3, 7, 4] 일 때, , i = 2, j = 5, k = 3 이면
# [5,2,6,3]를 정렬한 [2,3,5,6]에서 3번째는 5

array = [1, 5, 2, 6, 3, 7, 4]
commands=[[2, 5, 3], [4, 4, 1], [1, 7, 3]]


def solution(array, commands):
    answer = []
    for i in commands:
        tmp = []
        tmp = array[i[0]-1:i[1]]        # 슬라이싱 하여 리스트 할당
        tmp.sort()
        answer.append(tmp[i[2]-1])
    return answer

print(solution(array,commands))