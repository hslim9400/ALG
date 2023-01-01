def make_heap(num):
    global tree
    tree.append(num)
    num_idx = len(tree)-1
    while True:
        if not parent[num_idx]:
            break
        if tree[parent[num_idx]] > tree[num_idx]:
            tree[parent[num_idx]], tree[num_idx] = tree[num_idx], tree[parent[num_idx]]
            num_idx = parent[num_idx]
        else:
            break


T = int(input())
for test_case in range(1, T+1):
    N = int(input())
    tree = [0]
    left = [0] * (N+1)
    right = [0] * (N+1)
    parent = [0] * (N+1)
    num_list = list(map(int, input().split()))
    for i in range(1, N//2+1):
        left[i] = 2*i
        parent[2*i] = i
        if 2*i+1 > N:
            continue
        right[i] = 2*i+1
        parent[2*i+1] = i
    for i in range(N):
        make_heap(num_list[i])

    target_idx = len(tree)-1
    ans = 0
    while True:
        if not parent[target_idx]:
            break
        ans += tree[parent[target_idx]]
        target_idx = parent[target_idx]
    print(f'#{test_case} {ans}')