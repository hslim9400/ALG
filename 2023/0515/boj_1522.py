letter_list = list(input())
n = len(letter_list)
a_count = letter_list.count('a')

max_a = 0
for start in range(n):
    end = start + a_count

    if end >= n:
        current_a = letter_list[start:].count('a') + letter_list[:end-n].count('a')
    else:
        current_a = letter_list[start:end].count('a')

    if current_a == a_count:
        max_a = current_a
        break

    if current_a > max_a:
        max_a = current_a

print(a_count - max_a)
