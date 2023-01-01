T = int(input())
for test_case in range(1, T+1):
    str_1 = input()
    str_2 = input()

    max_count = 0
    str_1 = set(list(str_1))  # 중복되는 알파벳들을 제거
    for alp in str_1:  # 모든 알파벳에 대해
        alp_count = str_2.count(alp)  # 해당 알파벳의 개수를 확인
        if alp_count > max_count:  # 최댓값 갱신
            max_count = alp_count

    print(f'#{test_case} {max_count}')
