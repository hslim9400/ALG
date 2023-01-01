from collections import deque
# 뉴페이스가 왔을 때의 케이스 분류
# 뉴페이스가 누군가를 고르는 경우의 수(n-1)
# 뉴페이스가 누군가와 선물을 주고받는 경우 : Sn(n-2)경우가 생김
# 그렇지 않은 경우 : 뉴페이스의 선물을 받은 녀석이 뉴페이스가 되는 경우와 같음, Sn(n-1)경우가 생김
# 점화식 Sn(n) = (n-1) * (Sn(n-1) + Sn(n-2))
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