def solution(cap, n, deliveries, pickups):
    answer = 0
    deliveries = [0] + deliveries
    pickups = [0] + pickups
    left_deliveries = sum(deliveries)
    left_pickups = sum(pickups)
    pickup_idx = 0
    delivery_idx = 0

    for i in range(n, -1, -1):
        if not pickup_idx:
            if pickups[i]:
                pickup_idx = i
        if not delivery_idx:
            if deliveries[i]:
                delivery_idx = i
        if pickup_idx and delivery_idx:
            break

    while pickup_idx or delivery_idx:  # 둘 다 남지 않을 때 까지
        answer += max(delivery_idx, pickup_idx)*2
        current_deliveries = min(left_deliveries, cap)
        current_pickups = min(left_pickups, cap)
        left_deliveries -= current_deliveries
        left_pickups -= current_pickups

        while current_deliveries:
            target = min(deliveries[delivery_idx], current_deliveries)
            deliveries[delivery_idx] -= target
            current_deliveries -= target
            if not deliveries[delivery_idx]:
                while delivery_idx > 0:
                    delivery_idx -= 1
                    if deliveries[delivery_idx]:
                        break

        while current_pickups:
            target = min(pickups[pickup_idx], current_pickups)
            pickups[pickup_idx] -= target
            current_pickups -= target
            if not pickups[pickup_idx]:
                while pickup_idx > 0:
                    pickup_idx -= 1
                    if pickups[pickup_idx]:
                        break
    return answer

print(solution(4, 5, [1, 0, 3, 1, 2], [0, 3, 0, 4, 0]))