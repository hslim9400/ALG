from collections import deque

def mergesort(target):
    global ans

    n = len(target)
    if n < 2:
        return target

    left = target[:n//2]
    right = target[n//2:]
    sorted_left = deque(mergesort(left))
    sorted_right = deque(mergesort(right))
    if sorted_left[-1] > sorted_right[-1]:
        ans += 1

    sorted_target = []
    while sorted_left or sorted_right:
        if sorted_left and sorted_right:
            if sorted_right[0] < sorted_left[0]:
                sorted_target.append(sorted_right.popleft())
            else:
                sorted_target.append(sorted_left.popleft())
        else:
            if sorted_left:
                sorted_target.extend(sorted_left)
                sorted_left = []
            else:
                sorted_target.extend(sorted_right)
                sorted_right = []
    return sorted_target


T = int(input())
for test_case in range(1, T+1):
    N = int(input())
    target = list(map(int, input().split()))
    ans = 0
    target = mergesort(target)
    print(f'#{test_case}', target[N//2], ans)
