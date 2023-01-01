codes = {'AE': '[AE]', 'Ae': '[AE]', 'aE': '[ae]', 'ae': '[ae]', 'OE': '[OE]', 'Oe': '[OE]', 'oe': '[oe]', 'oE': '[oe]',
         'ct': '[ct]', 'ff': '[ff]', 'fi': '[fi]', 'fl': '[fl]', 'ffi': '[ffi]', 'ffl': '[ffl]', 's(long)': '[longs]',
         'si': '[longsi]', 'sh': '[longsh]', 'sl': '[longsl]', 'st': '[longst]', 'ssi': '[longssi]'}

P = int(input())

for test_case in range(P):
    target = input() + ' '
    new_word = ''
    s_stack = []
    flag = 0

    for i in range(len(target)):
        if flag:
            flag -= 1
            continue
        if target[i] == 's':

            if target[i+1] not in {' ', '.', "'", '"', '$', ';', ':', '?', '(', ')', '-', '<', '>',
                                   '=', '!', 'f', 'b', 'k'}:
        else:
            new_word += target[i]
    print(new_word)


