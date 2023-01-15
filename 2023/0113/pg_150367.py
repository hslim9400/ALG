from collections import deque
def solution(numbers):
    answer = []
    for number in numbers:
        if number == 1:
            answer.append(1)
            continue
        target = bin(number)[2:]
        target_length = 1
        n = 2
        while number >= n:
            target_length = (target_length+1)*2 - 1
            n = 2 ** target_length

        target = '0'*(target_length-len(target)) + target
        leaf_nodes = [[]]
        for i in range(1, target_length+1):
            if i % 2:
                leaf_nodes[-1].append(i)
                if len(leaf_nodes[-1]) == 2:
                    leaf_nodes.append([])
        queue = deque(leaf_nodes)

        while queue:
            current = queue.popleft()
            left, right = current[0]-1, current[1]-1
            parent = (left+right)//2
            if target[left] == '1' or target[right] == '1':
                if target[parent] == '0':
                    answer.append(0)
                    break
            if parent == (target_length+1) // 2 - 1:
                answer.append(1)
                break
            queue[-1].append(parent+1)
            if len(queue[-1]) == 2:
                queue.append([])

    return answer

print(solution([1, 2, 3, 4, 5, 6, 7, 8, 63, 111, 95]))