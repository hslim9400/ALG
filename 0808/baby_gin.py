T = int(input())

for test_case in range(1, T+1):
    num = int(input())
    nums = []
    for _ in range(6):  # while문 사용시 10의 배수가 들어오면 마지막 0을 받지 못한다?
        nums = [num % 10] + nums  # 10으로 나눈 나머지인 1의자리 수를 저장
        num = num//10  # 저장한 1의 자리를 제외한 나머지 숫자로 다시 실행

    counts = [0] * 12  # 런을 확인하기 위해 10, 11번 인덱스까지 추가

    for i in range(len(nums)):
        counts[nums[i]] = counts[nums[i]] + 1  # 0~9의 숫자가 몇개 씩 들어있는지 counts에 저장

    while True:
        for i in range(len(counts)):  # counts의 숫자에 대해 해당 숫자가 세개 있는지 확인
            if counts[i] >= 3:
                counts[i] = counts[i] -3
                break  # 있다면 없애고 다시 확인
        else:
            break  # 없다면 while 탈출

    while True:
        for i in range(len(counts)):  # counts의 숫자에 대해 연속하는 세개의 숫자가 모두 있는지 확인
            if (counts[i] >= 1) and (counts[i+1] >= 1) and (counts[i+2] >= 1):
                counts[i], counts[i+1], counts[i+2] = counts[i] - 1, counts[i+1] - 1, counts[i+2] - 1
                break  # 있다면 없애고 다시 확인
        else:
            break  # 없다면 while 탈출

    if sum(counts) == 0:  # counts에 0뿐이라면 여섯개 숫자가 트리플렛, 런으로만 구성되었다는 뜻 Baby Gin
        ans = 'Baby Gin'
    else:  # 아님 말고
        ans = 'Lose'

    print(f'#{test_case} {ans}')

