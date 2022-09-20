T = int(input())
for test_case in range(1, T+1):
    target = input()
    num = bin(int(target, 16))[2:]
    ans = '0'*(len(target)*4-len(num))+num
    for i in range(len(ans)//7):
        print(int(ans[7*i:7*(i+1)], 2), end=' ')
    print()

