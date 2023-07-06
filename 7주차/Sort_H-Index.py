def solution(citations):
    citations.sort()  # 오름차순 정렬
    n = len(citations)
    for i in range(n, 0, -1):  #오른쪽 인덱스에서부터 비교 반복
        if citations[i - 1] < n - (i - 1):
            return n - i
    return n

#return n 부분을 초기에는 0으로 설정 : 테스트케이스 9번 오류
#[10, 50, 100] 케이스를 생각하면 0이 아니라 논문의 개수인 n을 반환하는 게 맞음
