
T = int(input())
for test_case in range(T):

    N = int(input())
    line = list(input())  # 양보하지 않았을 때의 줄
    groups = {}
    total_waiting = 0  # 양보하지 않았을 때의 기다리는 시간
    for i in range(N-1, -1, -1):
        # 어떤 사람은 같은 그룹내의 가장 뒷 사람이 올때까지 기다려야 하므로
        # 줄의 마지막 인덱스부터 확인해주고
        # 리프트를 타기까지 기다리는 시간 + 내려서 마지막사람을 기다리는 시간
        # 을 더해준다.
        person = line[i]
        if person in groups.keys():
            groups[person].append(i)
            total_waiting += 5 * i
            total_waiting += (groups[person][0] - i) * 5
        else:
            # 그룹 내 마지막 사람이라면 리프트를 타기까지 시간만 더하면 된다.
            groups[person] = [i]
            total_waiting += 5 * i
    ideal_waiting = 5 * (N-1)*N // 2  # 잘 양보했을 때의 기다리는 시간
    for group in groups.keys():
        # 줄을 잘 서도 같은 그룹의 마지막 사람은 기다려야 하므로 
        # 그룹의 크기만큼의 시간을 더해준다.
        n = len(groups[group])
        ideal_waiting += 5 * (n-1)*n // 2

    print(total_waiting - ideal_waiting)
