import sys
sys.setrecursionlimit(100000)
def make_pre_order(in_start, in_end, post_start, post_end):
    global pre_ordered
    if in_end < in_start or post_end < post_start:
        return

    root = post_ordered[post_end]
    pre_ordered.append(root)

    root_idx = idxs[root]

    make_pre_order(in_start, root_idx-1, post_start, post_start-in_start+root_idx-1)
    make_pre_order(root_idx+1, in_end, post_end-in_end+root_idx, post_end-1)

N = int(input())
in_orderd = list(map(int, input().split()))
post_ordered = list(map(int, input().split()))

idxs = [0 for _ in range(N+1)]
for i in range(N):
    idxs[in_orderd[i]] = i

pre_ordered = []
make_pre_order(0, N-1, 0, N-1)
print(*pre_ordered)