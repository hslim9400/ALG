T = int(input())

for test_case in range(1, T+1):

    N = input()
    ans = 'impossible'
    for i in range(2, 10):
        target = str(i * int(N))
        num_list = list(N)
        for num in target:
            if num in num_list:
                num_list.remove(num)
                continue
            break
        else:
            ans = 'possible'
            break

    print(f'#{test_case} {ans}')

