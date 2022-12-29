

target = input()
first = True
second = True
stack_1 = []
stack_2 = []

for i in range(len(target)-1, -1, -1):
    if target[i] == '1':
        if not stack_1 or stack_1[-1] == '1':
            stack_1.append('1')


    else:
        if not target:
            if stack_2[-1] == '1':

            else:
                pass
        else:
            stack_1 = []
