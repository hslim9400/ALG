T = int(input())
for test_case in range(1, T+1):
    N = int(input())
    a = N // 50000
    N = N - a * 50000
    b = N // 10000
    N = N - b*10000
    c = N // 5000
    N = N - c*5000
    d = N // 1000
    N = N - d*1000
    e = N // 500
    N = N - e*500
    f = N // 100
    N = N - f*100
    g = N // 50
    N = N - g*50
    h = N // 10
    print(f'#{test_case}')
    print(a, b, c, d, e, f, g, h)
