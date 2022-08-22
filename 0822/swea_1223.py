T = 10
for test_case in range(1, T+1):
    N = int(input())
    target = list(input())
    opers = ['+', '*']  # 연산자는 두 개 뿐
    op_stack = []
    num_stack = []
    for i in target:
        if i in opers:
            op_stack.append(i)  # 연산자는 연산자 스택에
        else:
            num_stack.append(int(i))  # 숫자는 숫자 스택에 넣는다.

    ans = 0
    prev_num = num_stack.pop()  # 마지막 숫자를 처음 연산할 것
    while op_stack:
        current_op = op_stack.pop()  # 스택에서 연산자 하나
        current_num = num_stack.pop()  # 숫자하나를 각각 꺼낸다.
        if current_op == '+':  # 연산자가 +라면 지금까지의 숫자들을 답에 더하고
            ans += prev_num
            prev_num = current_num  # 다음 더하기가 나올때 까지 저장할 숫자를 갱신
        else:  # 연산자가 곱하기라면
            prev_num = prev_num * current_num  # 이전 더하기부터 저장했던 숫자들에 곱한다.

    ans += prev_num  # 마지막 남은 숫자덩이는 아직 더해지지 않았다.
    print(f'#{test_case} {ans}')