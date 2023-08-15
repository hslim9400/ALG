n = int(input())
answers = []

while n:

    rooms = [0]
    portals = [0] * (n+1)
    for i in range(1, n+1):
        info = input().split()
        content, money, next_rooms = info[0], int(info[1]), list(map(int, (info[2:-1])))
        portals[i] = next_rooms
        rooms.append([content, money])
    
    visited = {}
    if n == 1:
        if rooms[1][1] != 'T':
            stack = [(1, 0)]
    else:
        stack = [(1, 0)]
    answer = 'No'

    while stack:
        current, money = stack.pop()
        
        if current == n:
            answer = 'Yes'
            break
        
        if rooms[current][0] == 'L':
            money = max(money, rooms[current][1])
            visited[current] = money
        else:
            visited[current] = money
            money -= rooms[current][1]
        
        for destination in portals[current]:
            if destination not in visited.keys() or \
                money > visited[destination]:
                if rooms[destination][0] == 'T' and money < rooms[destination][1]:
                    continue
                stack.append((destination, money))
    

    answers.append(answer)

    n = int(input())

print('\n'.join(answers))