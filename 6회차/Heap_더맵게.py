# def solution(scoville, K):
# 섞은 음식의 스코빌 지수 = 가장 맵지 않은 음식의 스코빌 지수 + (두 번째로 맵지 않은 음식의 스코빌 지수 * 2)

# min-heap 이용해서(by heapify()) 부모 노드 값 꺼내
import heapq
scoville=[9,1,10,2,3,12]
K=7
cnt=0
num=len(scoville)
for j in range(num):
    heapq.heapify(scoville)
    min1 = heapq.heappop(scoville)
    min2 = heapq.heappop(scoville)
    min_num=min1+2*min2

    heapq.heappush(scoville,min_num)
    cnt+=1
    if min_num > K:
            break
    else: continue

print(cnt)
    


    
        
