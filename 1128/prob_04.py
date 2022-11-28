

def lca(edges, roots):
    n = len(edges) + 1
    answer = [0] * (n-1)
    adj = [[] for _ in range(n+1)]
    edge_dict = {}
    for i in range(len(edges)):
        edge_dict[tuple(edges[i])] = i
        adj[edges[i][0]].append(edges[i][1])
        adj[edges[i][1]].append(edges[i][0])

    parent = [0] * (n+1)
    children = [[] for _ in range(n+1)]
    rank = [-1] + [0] * n

    stack = [(1, 0)]
    visited = set()
    while stack:
        current, current_rank = stack.pop()
        if current in visited:
            continue
        visited.add(current)
        rank[current] = current_rank
        for destination in adj[current]:
            if destination not in visited:
                parent[destination] = current
                children[current].append(destination)
                stack.append((destination, current_rank+1))

    print(parent)
    print(children)
    print(rank)
    print(edge_dict)
    current_root = 1
    for root in roots:
        print(11, current_root, root)
        if rank[current_root] < rank[root]:
            target_rank = rank[current_root]
            current_node = root
            left_root = current_root
            while True:
                if (current_node, parent[current_node]) in edge_dict.keys():
                    answer[edge_dict[(current_node, parent[current_node])]] += 1
                else:
                    answer[edge_dict[(parent[current_node], current_node)]] += 1
                current_node = parent[current_node]
                if rank[current_node] == target_rank:
                    break

        elif rank[current_root] > rank[root]:
            target_rank = rank[root]
            current_node = current_root
            left_root = root
            while True:
                if (current_node, parent[current_node]) in edge_dict.keys():
                    answer[edge_dict[(current_node, parent[current_node])]] += 1
                else:
                    answer[edge_dict[(parent[current_node], current_node)]] += 1
                current_node = parent[current_node]
                if rank[current_node] == target_rank:
                    break
        else:
            current_node = current_root
            left_root = root
        current_nodes = [current_node, left_root]
        while True:
            left, right = current_nodes[0], current_nodes[1]
            print(22, left, right)
            if left == right:
                break
            current_nodes[0] = parent[left]
            current_nodes[1] = parent[right]
            if (current_nodes[0], left) in edge_dict.keys():
                answer[edge_dict[(current_nodes[0], left)]] += 1
            else:
                answer[edge_dict[(left, current_nodes[0])]] += 1
            if (current_nodes[1], right) in edge_dict.keys():
                answer[edge_dict[(current_nodes[1], right)]] += 1
            else:
                answer[edge_dict[(right, current_nodes[1])]] += 1

        current_root = root

        print(answer)


lca([[1,2], [1,3], [2,4], [2, 5], [3, 6], [4, 7]], [4, 6, 7, 1])