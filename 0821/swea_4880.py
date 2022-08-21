def play(left, right):
    if left[0] == right[0]:
        return left
    else:
        if left[0] - right[0] == 1 or left[0] - right[0] == -2:
            return left
        else:
            return right


def tournament(group, first, last):
    if first == last:
        return group[0]
    else:
        left_win = tournament(group[:(len(group)+1)//2], first, (last+first)//2)
        right_win = tournament(group[(len(group)+1)//2:], (last+first)//2+1, last)
        return play(left_win, right_win)


T = int(input())
for test_case in range(1, T+1):
    N = int(input())
    cards = list(map(int, input().split()))
    students = []
    for i in range(1, N+1):
        students.append([cards[i-1], i])
    winner = tournament(students, 1, N)

    print(f'#{test_case} {winner[1]}')