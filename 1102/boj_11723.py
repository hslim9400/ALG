import sys
M = int(input())
S = set()

for _ in range(M):
    operation = sys.stdin.readline().rsplit()
    if len(operation) == 2:
        target = int(operation[1])
        operation = operation[0]

        if operation == 'add':
            S.add(target)
        elif operation == 'check':
            if target in S:
                print(1)
            else:
                print(0)
        elif operation == 'toggle':
            if target in S:
                S.discard(target)
            else:
                S.add(target)
        else:
            S.discard(target)

    else:
        operation = operation[0]
        if operation == 'all':
            S = set(range(1, 21))
        else:
            S = set()
