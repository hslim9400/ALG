from collections import deque
# 어떤 칸의 좀비에게 폭탄을 사용할지에 대한 계산:
# 해당 좀비의 체력 > 공격력 * (총을 맞는 시간 - 지뢰 격발로 인한 딜 손실 시간)

# 총의 사거리까지는 지뢰격발에 의한 딜손실이 누적되기만 하므로 더해줌
# 그 뒤는 사거리만큼의 배열을 유지하며 지뢰를 사용할 경우 1, 아니면 0을 넣어 딜손실을 계산

L = int(input())
Ml, Mk = map(int, input().split())
C = int(input())
zombies = []
for _ in range(L):
    zombies.append(int(input()))
bomb_left = C
bomb_used = deque([0])
damage_loss = 0
ans = 'YES'
for i in range(min(Ml, L)):
    damage_loss += bomb_used[-1]
    if zombies[i] > Mk * (1 + i - damage_loss):
        if not bomb_left:  # 총으로 못 잡는데 지뢰도 없음
            ans = 'NO'
            break
        bomb_left -= 1
        bomb_used.append(1)  # 딜 손실 계산을 위한 배열
    else:
        bomb_used.append(0)
bomb_used.popleft()
if ans == 'YES':  # 아직 안 끝났다
    for i in range(Ml, L):
        if bomb_left >= L - i:
            break
        damage_loss += bomb_used[-1]
        lost = bomb_used.popleft()
        if lost:  # 이 경우 해당격발로 인한 딜 손실이 끝났음
            damage_loss -= 1
        if zombies[i] > Mk * (Ml - damage_loss):
            if not bomb_left:
                ans = 'NO'
                break
            bomb_left -= 1
            bomb_used.append(1)
        else:
            bomb_used.append(0)
print(ans)

