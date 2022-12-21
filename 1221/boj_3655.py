
T = int(input())
for test_case in range(T):

    N = int(input())
    line = list(input())
    groups = {}
    total_waiting = 0
    for i in range(N-1, -1, -1):
        person = line[i]
        if person in groups.keys():
            groups[person].append(i)
            total_waiting += 5 * i
            total_waiting += (groups[person][0] - i) * 5
        else:
            groups[person] = [i]
            total_waiting += 5 * i
    ideal_waiting = 5 * (N-1)*N // 2
    for group in groups.keys():
        n = len(groups[group])
        ideal_waiting += 5 * (n-1)*n // 2

    print(total_waiting - ideal_waiting)
