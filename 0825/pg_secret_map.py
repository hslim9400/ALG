def make_bin(num, n):
    rst = ''
    while num:
        if num % 2:
            rst = '1' + rst
        else:
            rst = '0' + rst
        num = num // 2
    if len(rst) < n:
        rst = '0' * (n-len(rst)) + rst
    return rst


def solution(n, arr1, arr2):
    answer = []
    new_map = [[0] * n for _ in range(n)]
    for i in range(n):
        line_1 = arr1[i]
        line_2 = arr2[i]
        line_1 = list(make_bin(line_1, n))
        line_2 = list(make_bin(line_2, n))
        for j in range(n):
            if line_1[j] == '0' and line_2[j] == '0':
                new_map[i][j] = ' '
            else:
                new_map[i][j] = '#'
        answer.append(''.join(new_map[i]))

    return answer

print(solution(5, [9, 20, 28, 18, 11], [30, 1, 21, 17, 28]))