T = int(input())
for test_case in range(1, T+1):
    target = input()
    N = len(target)
    codes = {
        '001101': 0,
        '010011': 1,
        '111011': 2,
        '110001': 3,
        '100011': 4,
        '110111': 5,
        '001011': 6,
        '111101': 7,
        '011001': 8,
        '101111': 9
    }
    num = bin(int(target, 16))[2:]
    ans = '0'*(len(target)*4-len(num))+num
    ans = ans[N//2:-N//2]
    for i in range(len(ans)//6):
        print(codes[ans[6*i:6*(i+1)]], end=' ')


