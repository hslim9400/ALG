
T = int(input())
for test_case in range(1, T+1):
    target = input()
    prior = {'*': 3, '/': 3, '+': 2, '-': 2, '(': 1}  # 연산자들의 우선순위
    ans = ''  # 문자열로 출력할 것
    stack = []
    for i in target:  # 입력받은 문자열(수식)에 대해 하나하나 확인
        if i.isnumeric():  # 숫자라면
            ans += i  # 그대로 붙임
        elif i == '(':  # 여는 괄호라면
            stack.append(i)  # 스택에 추가
        elif i == ')':  # 닫는 괄호라면
            while stack[-1] != '(':  # 짝이 맞는 여는 괄호를 만날때까지
                ans += stack.pop()  # 쌓인 연산자들을 푼다.
            stack.pop()  # 여는 괄호까지 빼내준다.
        else:
            while stack and prior[i] <= prior[stack[-1]]:
                # 연산자 우선순위를 고려하여 스택 가장 위에 있는 연산자를 확인하고
                ans += stack.pop()  # 우선순위 높은애들을 꺼내 붙이고
            stack.append(i)  # 현재 연산자를 넣어준다.
    while stack:  # 남은 연산자들을 후입선출로 붙여준다.
        ans += stack.pop()
    print(f'#{test_case} {ans}')
