def solution(key, lock):
    lock_2 = list(map(list, zip(*lock[::-1])))
    lock_3 = list(map(list, zip(*lock_2[::-1])))
    lock_4 = list(map(list, zip(*lock_3[::-1])))
    N = len(lock)
    M = len(key)
    l, r, u, d = N-1, 0, N-1, 0
    holes = False
    for i in range(N):
        for j in range(N):
            if not lock[i][j]:
                holes = True
                if i < u:
                    u = i
                if j < l:
                    l = j
                if i > d:
                    d = i
                if j > r:
                    r = j

    if not holes:
        return True

    h = d - u + 1
    w = r - l + 1
    s = max(h, w)
    problem_1 = [[0] * s for _ in range(s)]

    for i in range(s):
        for j in range(s):
            if i+u < N and j+l < N:
                problem_1[i][j] = lock[i+u][j+l]
            else:
                problem_1[i][j] = 1

    problem_2 = list(map(list, zip(*problem_1[::-1])))
    problem_3 = list(map(list, zip(*problem_2[::-1])))
    problem_4 = list(map(list, zip(*problem_3[::-1])))
    problem_set_1 = set()
    problem_set_2 = set()
    problem_set_3 = set()
    problem_set_4 = set()

    for i in range(s):
        for j in range(s):
            if not problem_1[i][j]:
                problem_set_1.add((i, j))
            if not problem_2[j][i]:
                problem_set_2.add((j, i))
            if not problem_3[i][j]:
                problem_set_3.add((i, j))
            if not problem_4[j][i]:
                problem_set_4.add((j, i))

    for i in range(M):
        key[i] = [0]*(s-1) + key[i] + [0]*(s-1)
    key = [[0]*(M+2*s-2) for _ in range(s-1)] + key + [[0]*(M+2*s-2) for _ in range(s-1)]

    for x in range(M+s-1):
        for y in range(M+s-1):
            key_set = set()
            for i in range(s):
                for j in range(s):
                    if key[x+i][y+j]:
                        key_set.add((i, j))
            for hole in problem_set_1:
                if hole not in key_set:
                    break
            else:
                return True
            for hole in problem_set_2:
                if hole not in key_set:
                    break
            else:
                return True
            for hole in problem_set_3:
                if hole not in key_set:
                    break
            else:
                return True
            for hole in problem_set_4:
                if hole not in key_set:
                    break
            else:
                return True

    return False

print(solution([[0, 0, 0], [0, 1, 0], [0, 1, 0]], [[1, 1, 1], [1, 1, 1], [0, 0, 0]]	))
