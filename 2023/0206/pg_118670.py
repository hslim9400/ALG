from collections import deque

def solution(rc, operations):
    answer = []
    # 안녕하세요
    top = deque([])
    bottom = deque([])
    left = deque([])
    right = deque([])
    center = deque([])
    for i in range(len(rc)):
        line = rc[i]
        left.append(line[0])
        right.append(line[-1])
        if i == 0:
            top = deque(line[1:-1])
        elif i == len(rc)-1:
            bottom = deque(line[1:-1])
        else:
            center.append(deque(line[1:-1]))

    def shift_row():
        nonlocal top, bottom, left, right, center
        left.appendleft(left.pop())
        right.appendleft(right.pop())
        center.appendleft(top)
        top = bottom
        bottom = center.pop()

    def rotate():
        nonlocal top, bottom, left, right
        top.appendleft(left.popleft())
        right.appendleft(top.pop())
        bottom.append(right.pop())
        left.append(bottom.popleft())

    for operation in operations:
        if operation == 'ShiftRow':
            shift_row()
        else:
            rotate()
    top.appendleft(left[0])
    top.append(right[0])
    answer.append(list(top))
    for i in range(len(center)):
        line = center[i]
        line.appendleft(left[i+1])
        line.append(right[i+1])
        answer.append(list(line))
    bottom.appendleft(left[-1])
    bottom.append(right[-1])
    answer.append(list(bottom))
    print(answer)
    return answer

solution([[1, 2], [3, 4], [5, 6]], ["Rotate", "ShiftRow"])