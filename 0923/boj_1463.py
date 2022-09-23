from collections import deque
N = int(input())
dp = [0] * (N+1)
dp[N] = 1
queue = deque()
queue.append(N)
while queue:
    current = queue.popleft()
    if current == 1:
        break
    for x in [current/3, current/2, current-1]:
        if x == int(x) and not dp[int(x)]:
            queue.append(int(x))
            dp[int(x)] = dp[current] + 1
print(dp[1]-1)
