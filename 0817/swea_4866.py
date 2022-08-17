T = int(input())
for test_case in range(1, T+1):
    target = input()
    stack = []
    brackets = ['(', '[', '{', ')', ']', '}']
    pairs = {'(': ')', '[': '[', '{': '}', ')': 0, ']': 0, '}': 0}
    for i in target:
        if i in brackets:
            stack.append(i)

    ans = 1
    if len(stack) % 2:
        print(f'#{test_case} 0')
        continue

    while stack:
        for i in range(len(stack)-1):
            if stack[i+1] == pairs[stack[i]]:
                del stack[i], stack[i]
                break
        else:
            ans = 0
            break
    print(f'#{test_case} {ans}')
