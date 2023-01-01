

T = int(input())

for test_case in range(T):
    orders = list(input())
    n = int(input())
    target = input()
    if target != '[]':
        target = list(map(int, target[1:-1].split(',')))
    reverse = False
    front_deletes = 0
    end_deletes = 0

    for order in orders:
        if order == 'R':
            reverse = not reverse
        else:
            if reverse:
                end_deletes += 1
            else:
                front_deletes += 1

    if front_deletes + end_deletes > n:
        print('error')
        continue
    if end_deletes:
        target = target[front_deletes:-end_deletes]
    else:
        target = target[front_deletes:]

    if reverse:
        if target != '[]':
            target = target[::-1]

    print(str(target).replace(' ', ''))
