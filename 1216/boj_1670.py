
N = int(input())

S = [1, 1, 2]

for n in range(3, N//2+1):
    if n % 2:
        Sn = 0
        for i in range(n//2):
            Sn += S[i] * S[n - 1 - i] * 2
            Sn %= 987654321
        Sn += S[n//2]*S[n//2]
    else:
        Sn = 0
        for i in range(n//2):
            Sn += S[i] * S[n-1-i] * 2
            Sn %= 987654321
    S.append(Sn % 987654321)
if N == 2 or N == 0:
    print(1)
else:
    print(S[-1])
