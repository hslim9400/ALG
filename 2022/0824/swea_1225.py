T = 10
for test_case in range(1, T+1):
    x = input()
    num_list = list(map(int, input().split()))
    # 10, 6, 12, 8, ...

    counts = 1
    while True:
        target = num_list.pop(0)
        target -= counts

        if target <= 0:
            target = 0
            num_list.append(target)
            break
        num_list.append(target)
        counts += 1
        if counts == 6:
            counts = 1

    print(f'#{test_case}', *num_list)