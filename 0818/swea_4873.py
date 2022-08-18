T = int(input())
for test_case in range(1, T+1):
    target = list(input())
    while True:
        clone = target[:]  # 문자열을 복사해준다.
        for i in range(len(clone)-1):
            if clone[i] == clone[i+1]:  # 만약 중복되는 문자가 있다면
                clone = clone[:i] + clone[i+2:]  # 두개만 제거
                break  # 인덱스오류를 고려하여 한 사이클에 한번만 실행
        if clone == target:  # 제거하지 못했다면 더 이상 없다.
            break
        target = clone  # 다음사이클을 위해 조작한 문자열을 저장
    print(f'#{test_case} {len(target)}')
