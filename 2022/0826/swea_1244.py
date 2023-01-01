def change_num(tries, current):
    global memo
    if (M-tries) % 2 == 0:
        num = int(''.join(map(str, current)))
        if num in memo:
            return
        memo.add(num)

    if tries == M:
        return

    for i in range(len(num_list)-1):
        for j in range(i+1, len(num_list)):
            current[i], current[j] = current[j], current[i]
            change_num(tries+1, current)
            current[i], current[j] = current[j], current[i]



T = int(input())
for test_case in range(1, T+1):
    num_list, M = input().split()
    num_list = list(map(int, num_list))
    M = int(M)
    memo = set()
    change_num(0, num_list)
    max_num = max(memo)
    print(f'#{test_case} {max_num}')
