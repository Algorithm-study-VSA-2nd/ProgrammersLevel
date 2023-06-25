import heapq
operations = ["I -45", "I 653", "D 1", "I -642","I 45", "I 97", "D 1", "D -1", "I 333"]

def solution(operations):
    answer = []
    heap = []
    for operation in operations:
        command, value = operation.split()
        value = int(value)
        if command == 'I':
            heapq.heappush(heap, value)
        elif command == 'D' and value == -1:
            if len(heap) != 0:
                heapq.heappop(heap)
        else:
            if len(heap) != 0:
                max_val = max(heap)
                heap.remove(max_val)
    if len(heap) == 0:
        return [0, 0]
    else:
        answer.append(max(heap))
        answer.append(min(heap))
        return answer

print(solution(operations))
