def rotate(prevm, N):  # 2차원 배열을 1회전하는 함수
    nextm = []
    for i in range(N):  # 빈 배열을 생성
        nextm.append([])
        for j in range(N):
            nextm[i].append('0')

    for i in range(N):
        for j in range(N):  # 회전시킨 배열의 행은 이전 배열의 열
            nextm[i][N - j - 1] = prevm[j][i]  # 열은 N-1에서 이전 배열의 행을 뺀 값

    return nextm


def concat(matrix, N):  # 출력을 위해 모아주는 함수
    for i in range(N):
        matrix[i] = ''.join(matrix[i])


T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    # ///////////////////////////////////////////////////////////////////////////////////
    N = int(input())
    origin = []
    once = []
    twice = []
    three_times = []

    for i in range(N):
        origin.append(list(input().split()))

    once = rotate(origin, N)  # 1회전
    twice = rotate(once, N)
    three_times = rotate(twice, N)

    concat(once, N)  # 애스터리스크로 출력 가능 할듯
    concat(twice, N)
    concat(three_times, N)

    case = '#' + str(test_case)
    print(case)
    for i in range(N):
        print(once[i] + ' ' + twice[i] + ' ' + three_times[i])