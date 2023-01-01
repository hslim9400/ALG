def half_sec(atoms, energy):
    dx = [0, 0, -1, 1]
    dy = [1, -1, 0, 0]
    new_atoms = {}
    collisions = {}
    for atom in atoms.keys():  # 원자들을 움직여준다.
        x, y, = atom
        d = atoms[atom][0]
        if -1000 <= x+dx[d]*0.5 <= 1000 and -1000 <= y+dy[d]*0.5 <= 1000:  # 지도를 넘어가면 원자를 없애는 백트래킹
            if (x+dx[d]*0.5, y+dy[d]*0.5) in new_atoms.keys():  # True라면 충돌이 일어나는 좌표
                if (x+dx[d]*0.5, y+dy[d]*0.5) in collisions.keys():
                    collisions[(x+dx[d]*0.5, y+dy[d]*0.5)].append(atoms[atom][1])
                else:  # collision에 처음 넣는 원자는 좌표에 도달한 두 번째 원자이므로
                    # 처음 그 좌표에 도달한 원자와 함께 넣어줘야 한다.
                    collisions[(x+dx[d]*0.5, y+dy[d]*0.5)] = [new_atoms[(x+dx[d]*0.5, y+dy[d]*0.5)][1], atoms[atom][1]]
            else:
                new_atoms[(x+dx[d]*0.5, y+dy[d]*0.5)] = atoms[atom]
    return collide(new_atoms, collisions, energy)


def collide(atoms, collisions, energy):  # 충돌하는 함수
    for atom in collisions.keys():
        energy += sum(collisions[atom])
        del atoms[atom]  # 충돌 끝나면 해당 좌표에는 원자가 없음
    return atoms, energy


T = int(input())
for test_case in range(1, T+1):
    N = int(input())
    atoms = {}
    for i in range(N):
        atom = list(map(int, input().split()))
        atoms[(atom[0], atom[1])] = [atom[2], atom[3]]  # 가상좌표에 방향, 에너지 저장

    energy = 0
    for t in range(0, 4000):  # 0.5초 단위로 한번 시행, -1000에서 1000까지 가는데 4000번 시행해야 함
        atoms, energy = half_sec(atoms, energy)

    print(f'#{test_case} {energy}')
