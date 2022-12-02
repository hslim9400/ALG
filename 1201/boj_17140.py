# 사용한 자료구조
# A: 문제에 나온대로의 2차원 배열
# target: R연산을 수행할 경우 A, C연산을 수행할 경우 A의 전치
# result: 연산을 수행한 뒤의 target


# 한 줄에 대해 문제대로 정렬하는 함수
# counting sort와 유사한 접근을 한다.
def remake(line, max_value):
    new_line = []
    temp = []  # 여기에 모아서 정렬한 후 new_line에 넣어줄 것
    counts = [0] * (max_value + 1)
    for num in line:
        counts[num] += 1

    for i in range(1, max_value+1):
        if not counts[i]:
            continue
        temp.append([i, counts[i]])
    temp.sort(key=lambda x: (x[1], x[0]))
    for pair in temp:
        new_line.extend(pair)
    return new_line


r, c, k = map(int, input().split())
r, c = r - 1, c - 1
A = []
rows = 2
columns = 2
for _ in range(3):
    A.append(list(map(int, input().split())))

transposed = False
answer = -1
for t in range(101):
    # 100초를 봐야 하므로 101까지 범위 설정
    if rows >= r and columns >= c and A[r][c] == k:
        answer = t
        break
    if columns > rows:
        target = list(map(list, zip(*A)))
        transposed = True
    else:
        target = A

    result = []
    max_length = 0
    for i in range(len(target)):
        max_value = max(target[i])
        result.append(remake(target[i], max_value)[:100])
        if len(result[-1]) > max_length:
            max_length = len(result[-1])

    for i in range(len(result)):
        result[i] += [0]*(max_length-len(result[i]))
    if transposed:
        rows = max_length - 1
        columns = len(result) - 1
        A = list(map(list, zip(*result)))
        transposed = False
    else:
        rows = len(result) - 1
        columns = max_length - 1
        A = result
print(answer)