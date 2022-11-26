
T = int(input())
for test_case in range(1, T+1):

    target = list(input())
    frog_dicts = {'c': 0, 'r': 0, 'o': 0, 'a': 0, 'k': 0} # 이상함을 감지하기 위한 딕셔너리
    ans = 0 # 답
    stack = 0  # 울고있는 개구리
    playing = 0  # 노는 개구리
    for i in target:
        frog_dicts[i] += 1
        if i == 'c':  # 새로운 개구리 소리
            stack += 1  # 울고있는 개구리 추가
            if playing:  # 놀고 있는 개구리가 있다면
                playing -= 1  # 놀던 놈이 우는걸로
            else:  # 없다면
                ans += 1  # 뉴페이스
        if i == 'k':  # 울음이 끝남
            stack -= 1
            playing += 1
        if not frog_dicts['c'] >= frog_dicts['r'] >= frog_dicts['o'] >= frog_dicts['a'] >= frog_dicts['k']:
            # 울음이 순서대로 오지 않았다면
            ans = -1
            break

    if not (frog_dicts['c'] == frog_dicts['r'] == frog_dicts['o'] == frog_dicts['a'] == frog_dicts['k']):
        # 끝났는데 뭔가 이상하다면
        ans = -1
    print(f'#{test_case} {ans}')
