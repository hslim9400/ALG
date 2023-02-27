from collections import deque
import heapq
def solution(stones, k):
    answer = 0
    heap = [-i for i in stones[:k]]
    heapq.heapify(heap)
    print(heap)
    queue = deque(stones[:k])
    current_max = max(queue)
    current_dict = {}
    for number in queue:
        if number in current_dict.keys():
            current_dict[number] += 1
        else:
            current_dict[number] = 1

    answer = current_max
    for stone in stones[k:]:
        out = queue.popleft()
        current_dict[out] -= 1
        queue.append(stone)
        if stone in current_dict.keys():
            current_dict[stone] += 1
        else:
            current_dict[stone] = 1
        if out == current_max:
            while True:
                heapq.heappop(heap)
                heap_max = -heap[0]
                if current_dict[heap_max]:
                    break
        heapq.heappush(heap, -stone)
        current_max = -heap[0]
        if answer > current_max:
            answer = current_max
        if stone > current_max:
            current_max = stone

    return answer

solution([2, 4, 5, 3, 2, 1, 4, 2, 5, 1]	, 3)