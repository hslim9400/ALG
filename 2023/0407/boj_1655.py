import heapq
import sys

N = int(int(sys.stdin.readline()))
num_list = []
left_heap = []
right_heap = []
mid = [int(int(sys.stdin.readline()))]
print(mid[0])

for _ in range(N-1):
    new = int(int(sys.stdin.readline()))
    if len(mid) == 1:
        if mid[0] < new:
            heapq.heappush(right_heap, new)
            right_least = heapq.heappop(right_heap)
            mid.append(right_least)
            mid.sort()
            print(mid[0])
        else:
            heapq.heappush(left_heap, -new)
            left_most = -heapq.heappop(left_heap)
            mid.append(left_most)
            mid.sort()
            print(mid[0])

    else:
        mid.append(new)
        mid.sort()
        heapq.heappush(left_heap, -mid[0])
        heapq.heappush(right_heap, mid[2])
        mid = [mid[1]]
        print(mid[0])


