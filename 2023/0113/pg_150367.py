from collections import deque
def solution(numbers):
    answer = []
    for number in numbers:
        if number == 1:
            answer.append(1)
            continue
        target = bin(number)[2:]  # 0b어쩌구에서 0b를 떼고
        target_length = 1
        n = 2
        while number >= n:
            # 비트 세두기
            target_length = (target_length+1)*2 - 1
            n = 2 ** target_length

        target = '0'*(target_length-len(target)) + target  # 남는 비트 0으로 채우기
        leaf_nodes = [[]]
        for i in range(1, target_length+1):
            # 이진트리 만들기
            # 홀수 인덱스는 리프노드가 되고
            # 왼 쪽부터 리프 두개씩 한 세트
            if i % 2:
                leaf_nodes[-1].append(i)
                if len(leaf_nodes[-1]) == 2:
                    leaf_nodes.append([])
        queue = deque(leaf_nodes)

        while queue:
            # 같은 부모를 두고있는 노드를 한 세트씩 꺼내면서 
            # 만약 자식이 1인데 부모가 0이다?
            # 만들 수 없는 숫자라는 것
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