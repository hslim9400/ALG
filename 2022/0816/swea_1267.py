for test_case in range(1, 11):
    V, E = map(int, input().split())
    edge_list = list(map(int, input().split()))
    adj = [[0] * (V + 1) for _ in range(V + 1)]
    ends = set()
    for i in range(E):
        start = edge_list[2*i]
        end = edge_list[2*i + 1]
        ends.add(end)
        adj[start][end] = 1

    vertex = list(range(1, V+1))
    for end in ends:
        vertex.remove(end)

    stack = []
    for start in vertex:
        stack.append(start)
    done = []
    while stack:
        current = stack.pop()
        if current in done:
            continue
        done.append(current)
        for target in range(1, V+1):
            if adj[current][target] and target not in done:
                for prev in range(1, V+1):
                    if adj[prev][target]:
                        if prev not in done:
                            break
                else:
                    stack.append(target)

    print(f'#{test_case}', *done)
