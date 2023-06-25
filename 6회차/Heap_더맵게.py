# def solution(scoville, K):
# 섞은 음식의 스코빌 지수 = 가장 맵지 않은 음식의 스코빌 지수 + (두 번째로 맵지 않은 음식의 스코빌 지수 * 2)
# min-heap 이용해서(by heapify()) 부모 노드 값 꺼내서
import heapq
def solution(scoville, K):
    cnt = 0
    heapq.heapify(scoville)
    while (1):
        if len(scoville) <= 1 and scoville[0] < K:
            return -1
        if scoville[0] >= K:
            break

        min1 = heapq.heappop(scoville)
        min2 = heapq.heappop(scoville)
        min_num = min1+2*min2

        heapq.heappush(scoville, min_num)
        cnt += 1
    return cnt