def solution(citations):
    answer = 0
    citations.sort(reverse=True)
    cnt = 1
    for i in range(len(citations)): # 최대 인덱스 = len(citation) -> for문 범위설정
        if citations[i] >= cnt:
            answer = cnt
        cnt += 1
    return answer

solution(citations=[3,0,6,1,5])