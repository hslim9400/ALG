import sys
sys.stdin = open('input.txt', 'r')

for test_case in range(10):
    pn = int(input())
    arr = []
    cross_sum1 = 0
    cross_sum2 = 0
    for i in range(100):  # 배열 받아오기
        num_line = list(map(int, input().split()))
        arr = arr + [num_line]
        cross_sum1 = cross_sum1 + num_line[i]  # 대각선 합 구하기
        cross_sum2 = cross_sum2 + num_line[-1-i]
    if cross_sum2 < cross_sum1:  # 대각선 합 중 큰 값을 최대값에 저장
        max_sum = cross_sum1
    else:
        max_sum = cross_sum2

    for i in range(100):  # 배열을 돌면서 행, 열의 합 구하고 최대값 갱신
        row_sum = 0
        column_sum = 0
        for j in range(100):
            row_sum = row_sum + arr[i][j]
            column_sum = column_sum + arr[j][i]
        if row_sum > max_sum or column_sum > max_sum:  # 최대값 갱신
            if row_sum > column_sum:
                max_sum = row_sum
            else:
                max_sum = column_sum

    print(f'#{pn} {max_sum}')

