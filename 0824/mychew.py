N = 20
counts = N -1
waiting = [1]
number = 1

while counts:
    waiting.append(waiting.pop(0))
    number += 1
    waiting.append(number)
    counts -= 1
    print(waiting)

print(waiting)