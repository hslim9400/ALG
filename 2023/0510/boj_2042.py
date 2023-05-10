def change_tree(idx, num):
  tree_idx = idx + k
  existing = segment_tree[tree_idx]
  segment_tree[tree_idx] = num
  current = tree_idx
  parent = current // 2
  
  while parent:
    segment_tree[parent] -= existing
    segment_tree[parent] += num
    current = parent
    parent //= 2
    
  return

def range_sum(current, start, end):
  if range_dict[current][0] >= start and range_dict[current][1] <= end:
    return segment_tree[current]
  if range_dict[current][0] > end or range_dict[current][1] < start:
    return 0
  
  return range_sum(current*2, start, end) + range_sum(current*2+1, start, end)

N, M, K = map(int, input().split())

k = 1
while k <= N:
  k *= 2
segment_tree = [0] * (k*2)
range_dict = {}
stack = [(1, [0, k-1])]
while stack:
  current, current_range = stack.pop()
  if current >= k:
    continue
  range_dict[current] = current_range
  stack.append((current*2, [current_range[0], (current_range[0]+current_range[1])//2]))
  stack.append((current*2+1, [(current_range[0]+current_range[1])//2+1, current_range[1]]))
for i in range(k, k*2):
  range_dict[i] = [i-k, i-k]

for i in range(N):
  num = int(input())
  change_tree(i, num)


for _ in range(M+K):
  a, b, c = map(int, input().split())
  if a == 1:
    change_tree(b-1, c)
  else:
    print(range_sum(1, b-1, c-1))