from collections import deque
# 그리디 알고리즘 적용
# 두 큐가 원상태로 복귀한다면 불가능 하다고 판단할 수 있다.

def solution(queue1, queue2):
    queue1 = deque(queue1)
    queue2 = deque(queue2)
    counts = 0
    total = 2 * len(queue1)
    sum_1 = sum(queue1)
    sum_2 = sum(queue2)
    while True:
        if sum_1 > sum_2:
            move = queue1.popleft()
            queue2.append(move)
            sum_1 -= move
            sum_2 += move
            counts += 1
        elif sum_1 < sum_2:
            move = queue2.popleft()
            queue1.append(move)
            sum_1 += move
            sum_2 -= move
            counts += 1
        else:
            break
        if counts > 2 * total:
            counts = -1
            break
        
    answer = counts
    return answer