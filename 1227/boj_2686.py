P = int(input())

for test_case in range(P):
    B = int(input())
    left = B
    target = ''
    while left:
        target += input()
        left -= len(target)//2
    print(target)
    ans = ''
    current = ''
    run = ''
    prev = ''
    counts = 0
    for i in range(B):
        sub_target = target[2*i:2*i+2]
        print(sub_target, current)
        if prev == '':
            continue
        current += sub_target
        if sub_target == prev:
            counts += 1
            if counts == 3:
                run = sub_target
                prefix = hex(len(current[:-2])//2)[2:].upper()
                ans += prefix
                ans += current
                current = run * 3
            if counts == 130:
                prefix = hex(counts - 3 + 128)[2:].upper()
                ans += prefix
                ans += run
                run = ''
                current = ''
        else:
            if counts >= 3:
                prefix = hex(counts - 3 + 128)[2:].upper()
                ans += prefix
                ans += run
                current = sub_target
            if len(current) == 256:
                prefix = hex(len(current[:-2]) // 2)[2:].upper()
                ans += prefix
                ans += current
                current = ''
        prev = sub_target
    print(len(ans)//2)
    print(ans)





