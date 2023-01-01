T = int(input())
for test_case in range(1, T+1):
    stack = []
    for i in input():
        if i == '(':  # 여는 괄호는 스택에 넣어준다.
            stack.append(i)
        else:
            # 닫는괄호라면 매칭되는 여는 괄호를 뽑는다. 먼저 나온 여는 괄호가 나중에 나온 닫는 괄호와 짝이다.
            try:
                stack.pop()
            except:  # 뽑아낼 여는 괄호가 없다면 짝이 맞지 않다. -1을 출력
                print(f'#{test_case} -1')
                break
    else:  # 모든 닫는 괄호에 대해 짝이되는 여는 괄호를 뽑았다면
        if not stack:  # 스택이 비어있어야 짝이 맞는다.
            print(f'#{test_case} 1')
        else:
            print(f'#{test_case} -1')
