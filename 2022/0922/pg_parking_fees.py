def solution(fees, records):
    answer = []
    min_time, min_fee, over_time, fee = fees
    parked = []
    cars = {}
    for record in records:
        record = record.split()
        target = record[1]
        if target not in cars.keys():
            cars[target] = 0
        if record[2] == 'OUT':
            for car in parked:
                if target == car[1]:
                    cars[target] += 60 * (int(record[0][:2]) - int(car[0][:2])) + (
                        int(record[0][-2:]) - int(car[0][-2:]))
                    parked.remove(car)
                    break
        else:
            parked.append(record)

    for car in parked:
        target = car[1]
        cars[target] += 60 * (23 - int(car[0][:2])) + (59 - int(car[0][-2:]))
    total_fees = []
    for car in cars.keys():
        if cars[car] > min_time:
            left = (cars[car] - min_time) // over_time
            if left:
                total_fee = min_fee + (left + 1) * fee
            else:
                total_fee = min_fee + left*fee
        else:
            total_fee = min_fee
        total_fees.append((car, total_fee))
    total_fees.sort()
    for total_fee in total_fees:
        answer.append(total_fee[1])

    return answer
