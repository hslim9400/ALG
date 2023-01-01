def solution(numbers, hand):
    ans = ''
    pad = {1: (0, 0), 2: (0, 1), 3: (0, 2), 4: (1, 0), 5: (1, 1), 6: (1, 2), 7: (2, 0), 8: (2, 1), 9: (2, 2), 0: (3, 1)}

    left = (3, 0)
    right = (3, 2)
    while numbers:
        number = numbers.pop(0)
        if number in [1, 4, 7]:
            ans += 'L'
            left = pad[number]
            continue
        elif number in [3, 6, 9]:
            ans += 'R'
            right = pad[number]
            continue
        else:
            l_dist = abs(left[0] - pad[number][0]) + abs(left[1] - pad[number][1])
            r_dist = abs(right[0] - pad[number][0]) + abs(right[1] - pad[number][1])
            if l_dist < r_dist:
                ans += 'L'
                left = pad[number]
            elif l_dist > r_dist:
                ans += 'R'
                right = pad[number]
            else:
                if hand == 'left':
                    ans += 'L'
                    left = pad[number]
                else:
                    ans += 'R'
                    right = pad[number]
    answer = ans
    return answer