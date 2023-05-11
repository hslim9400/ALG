N = int(input())
board = []

for _ in range(N):
  line = list(map(int, input().split()))
  board.append(line)
  
prefix_sum = [[0] * N for _ in range(N)]
prefix_sum[0][0] = board[0][0]

for i in range(1, N):
  prefix_sum[0][i] = prefix_sum[0][i-1] + board[0][i]
  prefix_sum[i][0] = prefix_sum[i-1][0] + board[i][0]

for i in range(1, N):
  for j in range(1, N):
    prefix_sum[i][j] = prefix_sum[i][j-1] + prefix_sum[i-1][j] - prefix_sum[i-1][j-1] + board[i][j]
  
max_sum = prefix_sum[-1][-1]

for i in range(N):
  for j in range(N):
    max_k = min(i+1, j+1)
    k = 1
    while k <= max_k:
      if i == k-1 and j == k-1:
        current_sum = prefix_sum[i][j]
      elif i == k-1:
        current_sum = prefix_sum[i][j] - prefix_sum[i][j-k]
      elif j == k-1:
        current_sum = prefix_sum[i][j] - prefix_sum[i-k][j]
      else:
        current_sum = prefix_sum[i][j] - prefix_sum[i-k][j] - prefix_sum[i][j-k] + prefix_sum[i-k][j-k]
      k+= 1
      max_sum = max(max_sum, current_sum)
print(max_sum)