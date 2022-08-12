T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    rows = []
    for _ in range(5):
        row = list(input())
        while True:
            if len(row) == 15:
                break
            row = row + ['']
        rows.append(row)
    rotated = list(zip(*rows))
    ans = ''
    for i in range(len(rotated)):
        ans = ans + ''.join(rotated[i])
    print(f'#{test_case} {ans}')