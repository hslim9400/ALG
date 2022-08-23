T = int(input())
for test_case in range(1, T+1):
    target = input().split()
    opers = ['+', '-', '*', '/']
    stack = []
    for i in target:
        if i == '.':  # 연산 종료
            if len(stack) != 1:  # 연산이 끝났는데 답이 없거나, 답외에 다른 숫자가 있는 경우
                ans = 'error'
                break
            ans = stack.pop()  # 답을 꺼낸다.
        elif i not in opers:  # 숫자라면 스택에 넣는다.
            stack.append(int(i))
        else:  # 연산자가 등장했을 경우
            if len(stack) < 2:  # 스택에 숫자가 한개이하면 연산할 수 없다.
                ans = 'error'
                break
            num_1 = stack.pop()
            num_2 = stack.pop()  # 이게 더 밑에있던 숫자. 즉, 먼저 입력된 숫자
            if i == '+':
                stack.append(num_2 + num_1)
            elif i == '-':
                stack.append(num_2 - num_1)
            elif i == '*':
                stack.append(num_2 * num_1)
            else:  # 나누어 떨어지는 수를 주고 결과를 정수로 출력해야 하므로
                stack.append(num_2 // num_1)

    print(f'#{test_case} {ans}')