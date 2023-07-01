N, K = map(int, input().split())

remainder = set()
multiplier = 1

while multiplier <= N:
    multiplier *= 10

current = N
answer = 1
while True:
    modulo = current % K

    if not modulo:
        break
    if modulo in remainder:
        answer = -1
        break
    remainder.add(modulo)
    current = N + (multiplier * modulo)
    answer += 1

print(answer)
