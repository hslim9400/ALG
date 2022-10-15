T = int(input())

for test_case in range(1, T+1):
    L, R, Q = input().split()
    n_l = len(L)
    n_r = len(R)
    L, R = int(L), int(R)
    targets = input().split()
    ans = ''
    for target in targets:
        # 주어진 접두사가 이미 최댓값보다 크다면 확인하지 않음
        # 0과 9를 하나씩 더해가며 어떤 자릿수로 만들 수 있는 최솟값과 최댓값을 가지고
        # 뭐라도 만들 수 있는게 확인되면 O, 무엇도 만들지 못한다면 다음자리로 넘어감(R의 자릿수까지)
        # 아무것도 못만들 경우 X
        if int(target) > R:
            ans += 'X'
            continue
        for adds in range(max(n_l-len(target), 0), n_r-len(target)+1):  # 확인해야하는 자릿수들 확인
            min_target = int(target + '0'*adds)  # 해당 자릿수에서 만들 수 있는 최솟값
            max_target = int(target + '9'*adds)  # 최댓값
            if L <= min_target <= R or L <= max_target <= R or\
                    min_target <= L <= max_target or min_target <= R <= max_target:
                # 위의 네 조건 중 하나만 해당되면 성공
                ans += 'O'
                break
        else:
            ans += 'X'

    print(f'#{test_case} {ans}')
