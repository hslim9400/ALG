T = int(input())
for test_case in range(1, T+1):
  p = [1, 1, 1, 2, 2, 3]
  N = int(input())
  if N > 6:
    for i in range(7, N+1):
      pn = p[-1] + p[-5]
      p.append(pn)
  print(f'#{test_case} {p[N-1]}')