def encode(is_run, target):

    code = ''
    if target == '':
        return ''

    if is_run:
        prefix = hex(counts - 3 + 128)[2:].upper()
        code += prefix
        code += target
    else:
        prefix = hex(len(target) // 2 - 1)[2:].upper()
        prefix = '0'*(2-len(prefix)) + prefix
        code += prefix
        code += target
    return code


P = int(input())

for test_case in range(P):
    B = int(input())
    left = B
    target = ''
    while left:
        line = input()
        target += line
        left -= len(line)//2
    ans = ''
    current = ''
    run = ''
    prev = ''
    counts = 0
    for i in range(B):
        sub_target = target[2*i:2*i+2]
        if prev == '':
            current += sub_target
            prev = sub_target
            counts = 1
            continue
        current += sub_target
        if sub_target == prev:
            counts += 1
            if counts == 3:
                run = sub_target
                ans += encode(False, current[:-6])
                current = run * 3
            if counts == 130:
                ans += encode(True, run)
                run = ''
                current = ''
                counts = 0
        else:
            if counts >= 3:
                ans += encode(True, run)
                current = sub_target
            counts = 1
            if len(current) == 256:
                ans += encode(False, current)
                current = ''
                counts = 0
        prev = sub_target
    if counts >= 3:
        ans += encode(True, run)
    else:
        ans += encode(False, current)

    print(len(ans)//2)
    pointer = 0
    while pointer < len(ans):
        print(ans[pointer:pointer+80])
        pointer += 80

