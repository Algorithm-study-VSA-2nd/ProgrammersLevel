import heapq
jobs=[[0,3],[2,6],[1,9]]

jobs.sort()
num=len(jobs)
count=[]    # 몇 초 걸렸는지
waiting=[] # waiting=[(소요시간,시작시점)]
now=0

while len(count) != num:
    while jobs and now >= jobs[0][0]:
        top = jobs.pop(0)
        heapq.heappush(waiting,(top[1],top[0]))

    if jobs and waiting == []:
        top = jobs.pop(0)
        now=top[0]
        heapq.heappush(waiting,(top[1],top[0]))

    x,y=heapq.heappop(waiting)
    now += x
    count.append(now-y)

print(sum(count)//num)


