def play(left, right):  # 가위바위보 승부
    if left[0] == right[0]:  # 비기면 왼쪽이 이긴걸로 한다.
        return left
    else:  # 1과 3이 승부하는 경우를 제외하면 숫자가 큰쪽이 이긴다.
        if left[0] - right[0] == 1 or left[0] - right[0] == -2:
            return left
        else:
            return right


def tournament(group, first, last):  # 토너먼트 그룹을 나눠 승자를 반환하는 함수 
    if first == last:  # 나눌 수 없다면
        return group[0]  # 부전승취급
    else:  # 왼쪽과 오른쪽으로 나눠 승자를 뽑아 겨룬다. 나누는 기준은 절반으로 나누되 홀수라면 왼쪽이 한명 더 많다.
        # 두명이라도 일단 나누어 내려보내고 부전승한셈 해서 올라와 겨룬다.
        left_win = tournament(group[:(len(group)+1)//2], first, (last+first)//2)  # 왼쪽 조의 승자
        right_win = tournament(group[(len(group)+1)//2:], (last+first)//2+1, last)  # 오른 쪽 조의 승자
        return play(left_win, right_win)  # 승자끼리 가위바위보를 해서 반환


T = int(input())
for test_case in range(1, T+1):
    N = int(input())
    cards = list(map(int, input().split()))
    students = []
    for i in range(1, N+1):
        students.append([cards[i-1], i])  # 가진 가위바위보 카드와 몇 번째 사람인지를 묶어서 저장
    winner = tournament(students, 1, N)  # 한명의 승자를 반환 할 것이다.

    print(f'#{test_case} {winner[1]}')