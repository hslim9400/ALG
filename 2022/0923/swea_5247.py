from collections import deque

T = int(input())

for test_case in range(1, T+1):
    N, M = map(int, input().split())
    count = 0
    flag = False
    queue = deque()
    queue.append((N, 0))
    visited = set()

    while queue:
        current = queue.popleft()
        num = current[0]
        if num in visited:
            continue
        visited.add(num)
        count = current[1]
        if num == M:
            ans = count
            break
        if num * 2 <= 1000000 and num*2 not in visited:
            queue.append((num*2, count+1))
        if num + 1 not in visited:
            queue.append((num+1, count+1))
        if num - 1 > 0 and num-1 not in visited:
            queue.append((num-1, count+1))
        if num - 10 > 0 and num-10 not in visited:
            queue.append((num-10, count+1))

    print(f'#{test_case} {ans}')
