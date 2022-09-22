T = int(input())

for test_case in range(1, T + 1):
    cards = list(map(int, input().split()))
    p_1 = []
    p_2 = []
    count_1 = [0] * 12
    count_2 = [0] * 12
    winner = 0
    flag = False
    for i in range(12):
        if i % 2:
            p_2.append(cards[i])
            count_2[cards[i]] += 1
        else:
            p_1.append(cards[i])
            count_1[cards[i]] += 1

        for i in range(10):
            if count_1[i] == 3:
                winner = 1
                flag = True
                break
            if count_1[i] and count_1[i + 1] and count_1[i + 2]:
                winner = 1
                flag = True
                break
            if count_2[i] == 3:
                winner = 2
                flag = True
                break
            if count_2[i] and count_2[i + 1] and count_2[i + 2]:
                winner = 2
                flag = True
                break
        if flag:
            break

    print(f'#{test_case} {winner}')
