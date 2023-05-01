def find_friend(x):
  if friends[x] == x:
    return x
  friends[x] = find_friend(friends[x])
  return friends[x]

def find_enemy(x):
  if not enemies[x]:
    return 0
  enemies[x] = find_friend(enemies[x])
  return enemies[x]
  
def is_enemy(x, y):
  x_enemy = find_enemy(x)
  y_enemy = find_enemy(y)
  
  if x_enemy and y_enemy and x_enemy == y_enemy:
    return False
  return True

def union_friend(x, y):
  x = find_friend(x)
  y = find_friend(y)
  
  if (x < y):
    friends[y] = x
  else:
    friends[x] = y
    
def union_enemy(x, y):
  enemies[x] = find_friend(y)
  enemies[y] = find_friend(x)
  
  
N, M = map(int, input().split())
print(N, M)
enemies = [0] * (N+1)
friends = list(range(N+1))
answer = 1

for _ in range(M):
  one, other = map(int, input().split())
  print(one, other)
  if not answer:
    continue
  union_enemy(one, other)
  print("enemies : ", enemies)
  if not is_enemy(one, other):
    answer = 0
  
  union_friend(one, find_enemy(other))
  union_friend(other, find_enemy(one))
  print("friends ", friends)
  print()
  
  
print(answer)