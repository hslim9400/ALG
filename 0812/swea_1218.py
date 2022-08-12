for test_case in range(1, 11):
    tc = int(input())
    target = input()
    prob = input()
    ans = 0

    for i in range(len(prob) - len(target) + 1):
        if prob[i:i + len(target)] == target:
            ans = ans + 1

    print(f'#{test_case} {ans}')