N = int(input())

if N < 8:
    if N == 3 or N == 5:
        ans = 1
    elif N == 6:
        ans = 2
    else:
        ans = -1
else:
    if N % 5 == 1:
        ans = N//5 - 1 + 2
    elif N % 5 == 2:
        ans = N//5 - 2 + 4
    elif N % 5 == 3:
        ans = N//5 + 1
    elif N % 5 == 4:
        ans = N//5 -1 + 3
    else:
        ans = N//5
print(ans)