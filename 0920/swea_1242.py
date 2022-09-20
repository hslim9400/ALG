import sys
sys.stdin = open("sample_input.txt", "r")

T = int(input())

for test_case in range(1, T+1):
    N, M = map(int, input().split())
    memo = set()
    ans = 0
    for _ in range(N):
        line = input().strip()
        for j in line:
            if j != '0':
                break
        else:
            continue
        target = ''
        for j in line:
            bin_num = str(bin(int(j, 16))[2:])
            target += '0'*(4-len(bin_num)) + bin_num

        while target:
            for k in range(M):
                if target[::-1][k] == '1':
                    end_idx = k
                    break
            else:
                break
            if end_idx == 0:
                target = target[:]
            else:
                target = target[:-end_idx]

            for stride in range(1, M):
                code_gen = [(3, 2, 1, 1), (2, 2, 2, 1), (2, 1, 2, 2), (1, 4, 1, 1), (1, 1, 3, 2), (1, 2, 3, 1), (1, 1, 1, 4),
                            (1, 3, 1, 2), (1, 2, 1, 3), (3, 1, 1, 2)]
                decoder = {}
                for i in range(10):
                    num_code = ''
                    for j in range(4):
                        if j % 2:
                            num_code += code_gen[i][j] * '1'
                        else:
                            num_code += code_gen[i][j] * '0'
                    decoder[num_code] = i
                last = target[-(stride*7):]
                if last in decoder.keys():
                    break
            current_target = target[-56*stride:]
            if current_target in memo:
                continue

            memo.add(current_target)
            target = target[:-56*stride]
            decoded = 0
            check = 0
            for i in range(8):
                num = decoder[current_target[7*i:7*i+7]]
                decoded += num
                if i%2:
                    check += num
                else:
                    check += num * 3
            if check % 10:
                ans += decoded
    print(ans)
