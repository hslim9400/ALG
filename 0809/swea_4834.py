
T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):

    N = int(input())

    deck = input()  # 숫자묶음
    nums = []
    for i in range(N):
        nums = nums + [int(deck[i])]  # 묶음에서 하나씩 뜯어 리스트에 저장
    counts = [0]*10
    ans = 0

    for i in range(N):
        counts[nums[i]] = counts[nums[i]] + 1  # 숫자의 개수를 센다


    for i in range(10):
        # 카운트가 가장 높은 숫자를 저장, 같은 개수면 뒤의 i가 크므로 더 큰 숫자가 답이 된다.
        if counts[i] >= counts[ans]:
            ans = i

    print(f'#{test_case} {ans} {counts[ans]}')