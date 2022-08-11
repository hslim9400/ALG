T = int(input())

for test_case in range(1, T+1):
    total_page, target_1, target_2 = list(map(int, input().split()))  # 책의 총 페이지, 두 사람의 목표 페이지
    l_1, r_1, l_2, r_2 = 1, total_page, 1, total_page  # 첫 조건, 1과 마지막 페이지가 된다
    c_1, c_2 = [int((l_1+r_1)/2)] * 2  # 가운데
    win = 0

    while True:
        if c_1 == target_1:  # 반복문 종료 조건, 둘 중 한명이 목표 페이지를 찾을 시(중간값이 목표페이지)
            win = 'A'
            break
        if c_2 == target_2:
            win = 'B'
            break

        if c_1 > target_1:  # 각각에 대해 이진탐색을 진행, 중간값이 목표보다 클 경우
            r_1 = c_1  # 그 부분이 오른쪽 끝이 된다.
            c_1 = int((l_1+r_1)/2)  # 다시 중간값을 찾는다.
        else:  # 작을경우 왼쪽이 된다.
            l_1 = c_1
            c_1 = int((l_1+r_1)/2)

        if c_2 > target_2:
            r_2 = c_2
            c_2 = int((l_2+r_2)/2)
        else:
            l_2 = c_2
            c_2 = int((l_2+r_2)/2)

    if c_1 == target_1 and c_2 == target_2:  # 만약 다른 한명도 목표 페이지를 찾았다면 비기게 된다.
        win = 0

    print(f'#{test_case} {win}')