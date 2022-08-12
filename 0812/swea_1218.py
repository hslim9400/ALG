for test_case in range(1, 11):
    tc = int(input())
    target = input()
    prob = input()
    ans = 0

    for i in range(len(prob) - len(target) + 1):  # 특정 문자열의 길이만큼 확인할 것이므로
        if prob[i:i + len(target)] == target:  # 문자열의 길이만큼 슬라이싱하여 확인
            ans = ans + 1

    print(f'#{test_case} {ans}')