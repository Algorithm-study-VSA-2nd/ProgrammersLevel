def solution(citations):
    answer = 0
    # 오름차순 배열로 정렬
    citations.sort()
    length = len(citations)
    for i in range(0,length):
        # h번 이상 인용된 논문이 h편 이상이라고 하였고 h-index라고 주어진 점이 핵심이다.
        if citations[i] >= length - i:
            answer = length - i
            # answer를 구하였으므로 break
            break
    return answer

