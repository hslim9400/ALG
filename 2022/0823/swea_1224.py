T = 10
for test_case in range(1, T+1):
    target = input()
    prior = {'*': 3, '+': 2, '(': 1}  # 연산자들의 우선순위
    postfix = ''  # 문자열로 출력할 것
    stack = []
    for i in target:
        if i.isnumeric():
            postfix += i
        elif i == '(':
            stack.append(i)
        elif i == ')':  # 닫는 괄호라면
            while stack[-1] != '(':  # 짝이 맞는 여는 괄호를 만날때까지
                postfix += stack.pop()  # 쌓인 연산자들을 푼다.
            stack.pop()  # 여는 괄호까지 빼내준다.
        else:
            while stack and prior[i] <= prior[stack[-1]]:
                # 연산자 우선순위를 고려하여 스택 가장 위에 있는 연산자를 확인하고
                postfix += stack.pop()  # 우선순위 높은애들을 꺼내 붙이고
            stack.append(i)  # 현재 연산자를 넣어준다.
    while stack:  # 남은 연산자들을 후입선출로 붙여준다.
        postfix += stack.pop()

    stack = []
    for i in postfix:  # 후위 표기법으로 변경된 식이 저장되어있다.
        if i.isnumeric():  # 숫자라면
            stack.append(i)  # 스택에 넣고
        else:  # 연산자라면
            num_1 = stack.pop()  # 나중에 등장한 숫자
            num_2 = stack.pop()  # 먼저 등장한 숫자
            if i == '+':  # 덧셈이면 더하고 곱셈이면 곱한다.
                stack.append(num_2 + num_1)
            else:
                stack.append(num_2 * num_1)

    print(f'#{test_case} {stack.pop()}')
