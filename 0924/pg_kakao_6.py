import sys

sys.setrecursionlimit(3000)


def solution(n, m, x, y, r, c, k):
    answer = 'impossible'
    directions = {'l': (0, -1), 'd': (1, 0), 'r': (0, 1), 'u': (-1, 0)}

    start = (x, y)
    end = (r, c)
    flag = False
    if (k - abs(r - x) - abs(c - y)) % 2:
        return answer

    def move(current, counts, word):
        nonlocal answer, flag
        if flag:
            return
        if counts == k:
            if current == end:
                answer = word
                flag = True
            return

        r = current[0]
        c = current[1]
        for d in ['d', 'l', 'r', 'u']:
            dr = directions[d][0]
            dc = directions[d][1]
            if abs(r + dr - end[0]) + abs(c + dc - end[1]) > k - counts:
                continue
            if 1 <= r + dr <= n and 1 <= c + dc <= n:
                move((r + dr, c + dc), counts + 1, word + d)

    move(start, 0, '')

    return answer