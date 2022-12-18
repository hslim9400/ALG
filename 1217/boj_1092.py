

N = int(input())
cranes = list(map(int, input().split()))
cranes.sort(reverse=True)

M = int(input())
boxes = list(map(int, input().split()))
boxes.sort(reverse=True)
ans = 0
if boxes[0] > cranes[0]:
    ans = -1

if not ans:

    while boxes:
        for i in range(len(cranes)):
            for j in range(len(boxes)):
                if cranes[i] >= boxes[j]:
                    del boxes[j]
                    break
        ans += 1
print(ans)
