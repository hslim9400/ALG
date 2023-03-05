from collections import deque


def solution(sales, links):
    answer = 0
    parents = [0] * (len(sales) + 1)
    children = [set() for _ in range(len(sales) + 1)]
    children_clone = [set() for _ in range(len(sales) + 1)]
    for link in links:
        parent, child = link
        parents[child] = parent
        children[parent].add(child)
        children_clone[parent].add(child)
    dp = [[0, 0] for _ in range(len(sales) + 1)]
    # [내가 갈때, 내가 안갈때]
    queue = deque([])
    for node in range(1, len(sales) + 1):
        if not children[node]:
            queue.append(node)
    while queue:
        current = queue.popleft()
        dp_1 = 0
        dp_2 = 0  # 내가 안갈 때 들어감
        if children[current]:
            children_dp = []
            min_diff = float('inf')
            for child in children[current]:
                children_dp.append(dp[child])
                if dp[child][0] - dp[child][1] < min_diff:
                    min_diff = dp[child][0] - dp[child][1]
            flag = False
            for child in children_dp:
                dp_1 += min(child)
                if child[0] - child[1] == min_diff:
                    if flag:
                        dp_2 += min(child)
                    else:
                        dp_2 += child[0]
                        flag = True
                    continue
                dp_2 += min(child)
                if min(child) == child[0]:
                    falg = True
        dp[current] = [dp_1 + sales[current - 1], dp_2]
        children_clone[parents[current]].discard(current)
        if not children_clone[parents[current]]:
            queue.append(parents[current])
        if current == 1:
            break
    answer = min(dp[1])

    return answer