def solution(users, emoticons):
    answer = []
    max_subs = 0
    max_money = 0
    discounts = [0] * len(emoticons)

    def discount(depth, discounts):
        nonlocal max_subs, max_money
        if depth == len(discounts):
            total_money = 0
            subscribe = 0
            for i in range(len(users)):
                money = 0
                for j in range(len(discounts)):
                    if discounts[j] >= users[i][0]:
                        money += int(emoticons[j] * (100 - discounts[j]) / 100)
                        if money >= users[i][1]:
                            subscribe += 1
                            break
                else:
                    total_money += money
            if subscribe > max_subs:
                max_subs = subscribe
                max_money = total_money
            elif subscribe == max_subs:
                if total_money > max_money:
                    max_money = total_money
            return

        new_discounts = discounts[:]
        for i in [10, 20, 30, 40]:
            new_discounts[depth] = i
            discount(depth + 1, new_discounts)

    discount(0, emoticons)
    answer = [max_subs, max_money]

    return answer

print(solution([[40, 10000], [25, 10000]], [7000, 9000]))
