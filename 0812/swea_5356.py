T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    rows = []
    for _ in range(5):
        row = list(input())
        while True:  # 문자열 길이가 최대 15이므로 zip을 활용하기 위해 전부 15로 맞춘다.
            if len(row) == 15:
                break
            row = row + ['']  # 내용이 변하면 안되므로 아무것도 없는 문자열을 추가
        rows.append(row)
    rotated = list(zip(*rows))  # zip으로 전치
    ans = ''
    for i in range(len(rotated)):  # 한줄로 출력하기 위해
        ans = ans + ''.join(rotated[i])
    print(f'#{test_case} {ans}')