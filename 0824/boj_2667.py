N = int(input())
town = []
for _ in range(N):
    town.append(list(map(int, list(input()))))
dr = [0, 1, 0, -1]
dc = [1, 0, -1, 0]

divs = [[]]
for i in range(N):
    for j in range(N):
        for div in divs:
            if town[i][j]:
                for d in range(4):
                    if (i+dr[d],j+dc[d]) in div:
                        div.append((i,j))
                        break
            else:
                break
        else:
            divs.append([(i,j)])

while True:
    flag = False
    for i in range(len(divs)-1):
        if flag:
            break
        for j in range(i+1, len(divs)):
            if len(divs[i]+divs[j]) != len(set(divs[i]+divs[j])):
                divs[i] = list(set(divs[i]+divs[j]))
                divs.remove(divs[j])
                flag = True
                break
    else:
        break
divs = divs[1:]
divs.sort(key= lambda x: len(x))
print(len(divs))
for div in divs:
    print(len(div))