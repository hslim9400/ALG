from collections import deque

N = int(input())
cards = deque(list(range(1, N+1)))
flag = True

while len(cards) > 1:
  if flag:
    cards.popleft()
    flag = False
  if not flag:
    cards.append(cards.popleft())
    flag = True
  
print(cards[0])