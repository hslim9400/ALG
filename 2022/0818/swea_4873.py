T = int(input())
for test_case in range(1, T+1):
    target = list(input())
    while True:
        for i in range(len(target)-1):
            if target[i] == target[i+1]:  # 만약 중복되는 문자가 있다면
                target = target[:i] + target[i+2:]  # 두개만 제거
                break  # 인덱스오류를 고려하여 한 사이클에 한번만 실행
        else:  # 제거하지 못했다면 더 이상 없다.
            break
    print(f'#{test_case} {len(target)}')
