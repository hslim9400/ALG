from collections import deque

N = int(input())

dp = deque([0, 1])
ans = 1
if N == 1:
    ans = 0
if ans:
    for i in range(2, N):
        dp.append(i*(dp[-1] + dp[-2]) % 1000000000)
        dp.popleft()
    ans = dp[-1]

print(ans)
