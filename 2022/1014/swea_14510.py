

T = int(input())
for test_case in range(1, T+1):

    N = int(input())
    trees = list(map(int, input().split()))

    trees.sort(reverse=True)
    target = trees[0]

    pointer = 0
    day = 1
    while pointer < N:
        for i in range(pointer, N):
            if trees[i] == target:
                trees[i], trees[pointer] = trees[pointer], trees[i]
                pointer += 1
                if pointer == N:
                    break
            else:
                if target - trees[i] == 1 and not (day % 2):
                    continue
                if target - trees[i] == 2 and day % 2 and target - trees[-1] <= 2:
                    continue
                trees[i] += (1 if (day%2) else 2)
                break
        day += 1
    print(f'#{test_case} {day-2}')



