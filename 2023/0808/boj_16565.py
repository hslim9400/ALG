N = int(input())

def factorial(k):
    fact = 1
    for i in range(1, k+1):
        fact *= i
    return fact

def combination(n, r):

    return factorial(n) // (factorial(r) * factorial(n-r))


dp = [[0] * 14 for _ in range(N+1)]
dp[0][0] = 1

for i in range(N):
    for j in range(13):
        for k in range(4):
            if i+k <= N:
                dp[i+k][j+1] = dp[i][j] * combination(4, k)

current = 1
answer = 0

while current*4 <= N:
    counts = combination(13, current)
    answer += counts * dp[N - 4*current][13-current]
    answer %= 10007
    current += 1

print(answer%10007)