def cycle(current, idx):
    if current[idx] == '1':
        current = current[:idx+1] + '0' * len(current[idx+1:])
    else:
        current = current[:idx+1] + '1' * len(current[idx+1:])
    return current


T = int(input())
for test_case in range(1, T+1):
    target = input()
    counts = 0
    current = '0' * len(target)

    for i in range(len(target)):
        if current[i] != target[i]:
            current = cycle(current, i)
            counts += 1
    print(f'#{test_case} {counts}')
