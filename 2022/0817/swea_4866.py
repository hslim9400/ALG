T = int(input())
for test_case in range(1, T+1):
    target = input()
    stack = []
    brackets = ['(', '[', '{', ')', ']', '}']
    pairs = {'(': ')', '[': '[', '{': '}', ')': 0, ']': 0, '}': 0}  # 짝을 찾기 위한 페어링
    for i in target:
        if i in brackets:  # 괄호들만 찾아 뽑아준다.
            stack.append(i)

    ans = 1  # 스택을 모두 비우면 짝이 잘 맞는 것
    if len(stack) % 2:  # 홀수라면 어차피 안맞으므로
        print(f'#{test_case} 0')
        continue

    while stack:
        for i in range(len(stack)-1):
            if stack[i+1] == pairs[stack[i]]:  # 가장 안쪽부터 (), [], {}로 완성되면 제거한다.
                del stack[i], stack[i]  # 하나를 없애므로 바로 다음 닫는 괄호도 i인덱스
                break
        else:  # 짝을 찾는데 실패
            ans = 0
            break
    print(f'#{test_case} {ans}')
