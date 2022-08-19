T = int(input())
for test_case in range(1, T+1):
    N, Q = map(int, input().split())
    boxes = [0] * N  # 0이 붙은 박스들을 만들어 놓고
    for i in range(1, Q+1):
        l, r = map(int, input().split())
        for j in range(l-1, r):  # 박스 번호는 1부터 시작하고, r을 포함하므로 레인지를 이렇게 잡는다.
            boxes[j] = i

    print(f'#{test_case}', *boxes)
