T = int(input())
for test_case in range(1, T+1):
    E, N = map(int, input().split())
    edges = list(map(int, input().split()))
    nodes = E + 1
    left = [0] * (nodes+1)
    right = [0] * (nodes+1)

    for i in range(E):
        start = edges[2*i]
        end = edges[2*i + 1]
        if left[start]:
            right[start] = end
        else:
            left[start] = end

    stack = [N]
    visited = []
    while stack:
        current = stack.pop()
        visited.append(current)
        if left[current]:
            stack.append(left[current])
        if right[current]:
            stack.append(right[current])

    print(f'#{test_case} {len(visited)}')
