
target = input()
prev = target[0]
stack = [prev]
proper = True
answer = 'SUBMARINE'
for i in range(1, len(target)):

    current = target[i]

    if current == '1':

        if not stack:
            proper = False
            stack.append(current)
            continue

        if stack == ['1']:
            answer = "NOISE"
            break

        if prev == '0':
            if stack == ['0']:
                stack = []
            else:


    else:
        if
